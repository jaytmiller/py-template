"""Top level library module.
"""

import os
import subprocess
from pathlib import Path
import stat

# from shutil import chown
import json

import filelock

from {{PYT_PKG_NAME}}.types import
from {{PYT_PKG_NAME}}.log import Log

# -----------------------------------------------------------------------------------------
#                                Globals
# -----------------------------------------------------------------------------------------
SVC_UID = os.environ.get("SVC_UID", "{{PYT_PKG_NAME}}")
SVC_GID = os.environ.get("SVC_GID", "{{PYT_PKG_NAME}}")
ROOT_DIR = Path(os.environ.get("PYT_PKG_NAME_ROOT_DIR", "/services/{{PKT_PKG_NAME}}"))

# -----------------------------------------------------------------------------------------


def run(cmd, cwd=".", timeout=30, check=True):
    """Run subprocess `cmd` in dir `cwd` failing if not completed within `timeout` seconds
    of if `cmd` returns a non-zero exit status.

    Returns both stdout+stderr from `cmd`.  (untested, verify manually if in doubt)
    """
    # Log().info(f"Running command: {cmd.split()}")
    return subprocess.run(
        cmd.split(),
        capture_output=True,
        text=True,
        check=check,
        cwd=cwd,
        timeout=timeout,
    )  # maybe succeeds


# -----------------------------------------------------------------------------------------
#                  API Class Implementing High Level Functions of {{PYT_PKG_NAME}}
# -----------------------------------------------------------------------------------------


class Api(self):
    """Maintains copies of users and groups in memory,  as well as a log
    interface and a lock to ensure that multiple spawners are not modifying
    the file store at the same time.
    """

    def __init__(self):
        self.log = Log()
        self.lock = filelock.FileLock(ROOT_DIR / "{{PYT_PKG_NAME}}.lock")
        self.flush_to_disk()
        ROOT_DIR.mkdir(parents=True, exist_ok=True)


    def main(self, *args, **keys):
        """
        """
        try:
            setup()
        except Exception as e:
            self.log.exception("{{PYT_PKG_NAME}} invalid parameter:", e)
            raise
        try:
            self.lock.acquire(blocking=True)
            return self._main(*args, **keys)
        except Exception as e:
            self.log.exception("{{PYT_PKG_NAME}} top level exception:", e)
            raise
        finally:
            self.lock.release()

    def _main(self, *args, **keys):
        self.log.info(">>>>> Called:", "main({args}, {keys})")
        self.log.info("<<<<< Returning:", info)
        return info

    def flush_to_disk(self) -> None:
        """Write out the following:
        """
        pass

# -----------------------------------------------------------------------------------------
#                            API Singleton and Convenience Functions
# -----------------------------------------------------------------------------------------

{{PYT_PKG_NAME}}_API: Api | None = None


def init_api(reinit: bool = False) -> {{PYT_PKG_NAME}}Api:
    """Initialize the {{PYT_PKG_NAME}} singleton."""
    global {{PYT_PKG_NAME}}_API
    if reinit or not {{PYT_PKG_NAME}}_API:
        {{PYT_PKG_NAME}}_API = {{PYT_PKG_NAME}}Api()
    return {{PYT_PKG_NAME}}_API


def main(*args, **keys)
) -> Info:
    """Simple function interface for main."""
    api = init_api(reinit=False)
    return api.main(*args, **keys)
