"""This module defines the client interface called by users of {{PYT_PKG_NAME}}
service.  These client calls perform HTTP requests to the server
which in turn calls the true {{PYT_PKG_NAME}} service code.
"""

import os
import requests
import functools

from {{PYT_PKG_NAME}}.types import Info


SERVICE_URL = os.environ.get("CLIENT_URL", "http://127.0.0.1:5050")

LRU_CACHE_SIZE = 1024

# -------------------------------------------------------------------------------------


def check_alive(service_url=SERVICE_URL, timeout=30):
    response = requests.get(service_url + "/check-alive", timeout=timeout)
    assert response.status_code == 200
    return response.json()


def main(*args, service_url=SERVICE_URL, timeout=30, **keys) -> Info:
    # Do input checks but keep simple objects for JSON serialization.
    data = dict(rval=keys["info"])

    print("{{PYT_PKG_NAME}} inputs: ", data)

    response = requests.post(
        service_url + "/main", json=data, timeout=timeout
    )

    if response.status_code == 200:
        info = Info(**response.json())
        print("{{PYT_PKG_NAME}} main output: ", info)
        return info
    else:
        raise Exception(f"Failed to main info: {response.text}")
