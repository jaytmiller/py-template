#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

def load_requirements(filename):
    with open(filename) as file:
        return file.read().splitlines()

requirements = load_requirements("requirements.txt")

test_requirements = load_requirements("test_requirements.txt")

setup(
    author="Todd Miller",
    author_email='none',
    python_requires='>=3.11',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    description="",
    install_requires=requirements,
    license="none",
    long_description=readme,
    include_package_data=True,
    keywords='{{PYT_PKG_NAME}}',
    name='{{PYT_PKG_NAME}}',
    packages=find_packages(include=['{{PYT_PKG_NAME}}', '{{PYT_PKG_NAME}}.*']),
    test_suite='tests',
    tests_require=test_requirements,
    extras_require = {
        "test": test_requirements,
    },
    url='none',
    version='0.1.0',
    zip_safe=False,
)
