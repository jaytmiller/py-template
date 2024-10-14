"""Top level library module"""

from .test_service import test_what_to_test as what_to_test


def test_what_to_test_svc(benchmark):
    benchmark(what_to_test)
