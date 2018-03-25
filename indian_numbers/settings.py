"""
app specific settings file
"""
import sys

from django.conf import settings

"""
version of python being used
"""
INDIAN_NUMBERS_PY_VERSION = None

"""
os/platform on which code is running

For Python2.7, Linux2.x and Linux3.x are reported as "linux2".
For Python3.3+, Linux2.x and Linux3.x are reported as "linux".
"""
INDIAN_NUMBERS_PLATFORM_NAME = None


def get(key, default):
    return getattr(settings, key, default)

py_version = sys.version_info
INDIAN_NUMBERS_PY_VERSION = get('INDIAN_NUMBERS_PY_VERSION', py_version)

platform_name = sys.platform
INDIAN_NUMBERS_PLATFORM_NAME = get('INDIAN_NUMBERS_PLATFORM_NAME', platform_name)

