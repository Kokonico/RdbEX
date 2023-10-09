from replit import db

from . import _var
from ._var import ban, config

protected_header = _var.protected_header

def db_grab(keyname):
  try:
    key = db[keyname]
    return key
  except KeyError:
    raise KeyError("key '" + splice_msg(keyname) + "' does not exist" ) from KeyError


def check_protection(keyname):
  if keyname[0:2] == protected_header:
    raise KeyError("Key is protected!")
  return False

def splice_msg(path):
  splitted = path.split("#")
  return splitted[len(splitted) - 1]
  
def valcheck(value):
  for i in value:
    if i in ban:
      raise KeyError("character not allowed: " + i)
  return False

def root(inpath):
  newpath = splice_msg(inpath)
  if newpath[0] != config["sep"]:
    newpath = config["sep"] + inpath
  if newpath[len(newpath) - 1] != config["sep"]:
    newpath = newpath + config["sep"]
  return newpath.split(config["sep"])