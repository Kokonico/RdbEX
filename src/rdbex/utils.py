"""utilites for RdbEX, to be used for interacting with the db."""

from packaging import version
from replit import db

from rdbex import __version__

from .__internal import _func, _var
from .__internal._var import config


def is_reference(value):
  """check if the received input is a reference command.
  good for protecting yourself against injections attacks."""
  if isinstance(value, str):
    return value[:len(config["ref"])] == config["ref"]
  else:
    return False


def key_exists(key: str, path: str = config["sep"]):
  """check if a given key exists within the db"""
  inpath = _var.msg + config["sep"].join(_func.root(path))
  res = True
  try:
    _func.db_grab(inpath + key)
  except KeyError:
    res = False
  return res


def repair():
  """attempts to repair the rdbex metadata. is non-destructive."""

  try:
    new_meta = _var.meta
    new_config = _var.config
  except KeyError:
    db[_var.protected_header + "rdbexmeta"] = {
        "config": _var.config_def,
        "version": __version__
    }
  
  new_meta = _var.meta
  new_config = _var.config
    
  for key in _var.config_def:
    if key not in _var.config:
      new_config[key] = _var.config_def[key]
  new_meta["config"] = new_config

  package_ver = version.parse(__version__)
  db_ver = version.parse(_var.meta["version"])

  if package_ver != db_ver:
    new_meta["version"] = str(package_ver)

  db[_var.protected_header + "rdbexmeta"] = new_meta



def configure(option, value):
  new_config = _var.config
  new_meta = _var.meta
  if option in _var.config_def:
    if option == "banned_chars":
      if isinstance(value, list):
        new_config[option] = value
      else:
        raise ValueError("value is not a list!")
    else:
      new_config[option] = value

    new_meta["config"] = new_config

    db[_var.protected_header + "rdbexmeta"] = new_meta
  else:
    raise NotImplementedError("invalid config option")
