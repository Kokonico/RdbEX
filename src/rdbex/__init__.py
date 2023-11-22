"""Adds a significant amount of features to replit’s preexisting database."""

import datetime
import os
import sys

from replit import db

from . import recovery
from .__internal import _recovery

__version__ = "0.2.6"

try:
    from . import utils
    from .__internal import _var
    from .RdbEX import DBcontroller

    utils.repair()
except KeyError as e:
    recovery.repair(False)
    # check if it's whining about the metadata key
    if e.args[0] == '>>rdbexmeta':
        print("RdbEX Metadata Key Missing. creating...")
        recovery.repair(False)
    else:
        raise ImportError(
            """critical damage to rdbex detected. 
        a repair has been ran, please restart.
        if the error persists, use "from rdbex import recovery" 
        and run recovery.rebuild() to attempt to fix the issue"""
        ) from KeyError
except ImportError:
    raise ImportError(
        """The package has been installed incorrectly and/or has been corrupted. 
    please reinstall the package."""
    ) from FileNotFoundError
