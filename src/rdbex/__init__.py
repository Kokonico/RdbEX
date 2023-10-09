"""Adds a significant amount of features to replit’s preexisting database."""

import datetime
import os
import sys

from replit import db
from . import recovery

__version__ = "0.2.0"

try:
    from . import utils
    from .__internal import _var
    from .RdbEX import db_list, delete, drop, read, reference, set
except KeyError:
    recovery.repair()
    raise ImportError("""critical damage to rdbex detected. 
    a repair has been ran, please restart.
    if the error persists, use "from rdbex import recovery" 
    and run recovery.rebuild() to attempt to fix the issue"""
                     ) from None
except FileNotFoundError:
    raise ImportError("""The package has been installed incorrectly and/or has been corrupted. please reinstall the package.""") 

utils.repair()

