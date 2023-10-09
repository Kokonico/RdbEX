"""recovery for RdbEX."""
from replit import db

from .__internal import _recovery


def rebuild():
  """completely rebuild the rdbex metadata, will delete all config data."""
  db[_recovery.protected_header + "rdbexmeta"] = {
    "config": _recovery.config_def,
    "version": "0.0.0"
  }
  print("rebuild complete. please reload RdbEX.")



def repair():
  """attempt to repair RdbEX without metadata loss."""

  meta = {}
  try:
    meta = db[_recovery.protected_header + "rdbexmeta"]
  except KeyError:
    rebuild()
    meta = db[_recovery.protected_header + "rdbexmeta"]
    
  # engage repair
  if "config" in meta.keys(): # repair version
    for i in _recovery.config_def:
      if i not in meta["config"]:
        meta["config"][i] = _recovery.config_def[i]
  else:
    meta["config"] = _recovery.config_def

  if "version" not in meta.keys():
    meta["version"] = "0.0.0"

  # push repaired result

  db[_recovery.protected_header + "rdbexmeta"] = meta
  print("repair completed successfully. please reload RdbEX.")