PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint lint/flake8 lint/black build push build-and-push
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

define TEST_OUTPUTS
{{PYT_PKG_NAME}}
endef
export TEST_OUTPUTS

BROWSER := python -c "$$BROWSER_PYSCRIPT"
TAG := "{{PYT_PKG_NAME}}"
#BASE_IMAGE_REPO := "${ECR_REGISTRY}/${IMAGE_REPO}"
BASE_IMAGE_REPO := "public.ecr.aws/docker/library/"
BASE_IMAGE_NAME := "python:3.12-slim"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clean-other ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -fr .pytest_cache
	rm -fr $$TEST_OUTPUTS

clean-other:
	rm -rf prof
	rm -f .coverage
	rm -fr htmlcov/
	rm -rf .mypy_cache

lint/flake8: ## check style with flake8
	find {{PYT_PKG_NAME}} tests service_tests -name '*.py' | xargs flake8  --max-line-length 120 \
	  --ignore E302,E203,E305,W291,W503,W504,W391,E501 --count  --statistics

lint/black: ## check style with black
	black --check {{PYT_PKG_NAME}} tests service_tests

lint/bandit: ## check security with bandit
	find {{PYT_PKG_NAME}} tests service_tests -name '*.py' | xargs bandit -v -ll -ii --format txt

lint/mypy:
	mypy --install-types  {{PYT_PKG_NAME}}

lint: lint/flake8  lint/mypy  lint/black  lint/bandit ## check style, type annotations, whitespace


build-and-push:  build  push

build:
	image-login
	docker build . --platform ${PLATFORM} --progress plain --build-arg BASE_IMAGE_NAME=${BASE_IMAGE_NAME} --build-arg BASE_IMAGE_REPO=${BASE_IMAGE_REPO} -t ${TAG} -t ${ECR_REGISTRY}/${IMAGE_REPO}:${TAG}

push:
	image-login
	docker push ${ECR_REGISTRY}/${IMAGE_REPO}:${TAG}
	docker images --digests | grep ${ECR_REGISTRY}/${IMAGE_REPO} | grep ${TAG} | awk '{ print $$3 }'

test-all: lint local-test service-test

test: local-test

local-test:  clean-test   ## run tests quickly with the default Python
	./local-test pytest

coverage: clean-test ## check code coverage quickly with the default Python
	./local-test coverage
	$(BROWSER) htmlcov/index.html

service-test: clean-test
	./service-test

load-test: clean-test
	./service-test load-test

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install
