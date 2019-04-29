# -*- coding: utf-8 -*-

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import sys
assert sys.version_info > (3, 5), "Python 2 detected, Cascabel requires Python >= 3.5 to run."

from . import api
