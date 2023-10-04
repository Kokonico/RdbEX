import importlib
import os

from replit import db

from rdbex import config

# internal variables

methods = [
  "FROM",
  "SECRET"
]

protected_header = ">>" # not to be used by normal people

ban = ["#", " ", "[", "]", "{", "}", "(", ")", ">", "<", config.sep] + config.banned_characters

msg = config.msg + "#"

# internal functions
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
  if newpath[0] != config.sep:
    newpath = config.sep + inpath
  if newpath[len(newpath) - 1] != config.sep:
    newpath = newpath + config.sep
  return newpath.split(config.sep)
  
# public functions
    
def set(key: str, value, path: str = config.sep):
  """create or set a key under the specified path."""
  valcheck(key)
  valcheck(root(path))
  inpath = msg + config.sep.join(root(path))
  db[inpath + key] = value

def delete(key: str, path: str = config.sep):
  """delete an existing key under the specified path."""
  valcheck(key)
  valcheck(root(path))
  inpath = msg + config.sep.join(root(path))
  del db[inpath + key]
  
def list(path: str = config.sep, removeprefix: bool = True, sortbydirs: bool = False):
  "list all keys within a path"
  prefix = config.sep.join(root(path))
  selected_keys = db.prefix(msg + prefix)
  result_list = []
  intermediate=[]
  for i in selected_keys:
    if removeprefix:
      intermediate.append(i.removeprefix(msg + prefix))
    else:
      intermediate.append(i)

  for i in intermediate:
    if sortbydirs:
      dirsplit = i.split(config.sep)

      if dirsplit[0] + config.sep not in result_list:
        result_list.append(dirsplit[0] + config.sep)

    else:
      result_list.append(i)
  return result_list


def drop(path: str = config.sep):
  "drop all values within a path"
  valcheck(root(path))
  
  for i in list(path, False):
    del db[i]

def reference(method: str, input, path: str = config.sep):
  """generate a reference string under a specified method,
  one or two inputs may be required"""
  mu = method.upper()
  ref = ""
  header = config.ref + mu + " "
  if mu not in methods:
    raise ValueError("bad method")
  if mu == "FROM":
    ref = header + config.sep.join(root(path)) + " " + input
  elif mu == "SECRET":
    ref = header + input
  return ref


def read(key: str, path: str = config.sep):
    inpath = config.sep.join(root(path))
    value = db[msg + inpath + key]
    if isinstance(value, str):
        if value[:3] == config.ref:
            value = value[3:]
            cmd = value.split()[0]
            if cmd == "FROM":
                vpath = value.split()[1]
                vkey = value.split()[2]
                return read(vkey, vpath)
            elif cmd == "SECRET":
              return os.environ[value.split()[-1]]
            
    else:
        return value