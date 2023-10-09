import importlib
import os

from replit import db

from rdbex import utils

from .__internal._func import check_protection, db_grab, root, splice_msg, valcheck
from .__internal._var import ban, config, methods, msg, protected_header
  
    
def set(key: str, value, path: str = config["sep"]):
  """create or set a key under the specified path."""
  valcheck(key)
  valcheck(root(path))
  inpath = msg + config["sep"].join(root(path))
  db[inpath + key] = value

def delete(key: str, path: str = config["sep"]):
  """delete an existing key under the specified path."""
  valcheck(key)
  valcheck(root(path))
  inpath = msg + config["sep"].join(root(path))
  del db[inpath + key]
  
def db_list(path: str = config["sep"], sortbydirs: bool = False, removeprefix: bool = True):
  "list all keys within a path"
  prefix = config["sep"].join(root(path))
  selected_keys = db.prefix(msg + prefix)
  result_list = []
  intermediate=[]
  for i in selected_keys:
    if removeprefix:
      intermediate.append(i.removeprefix(msg + prefix))
    else:
      intermediate.append(i.removeprefix(msg))

  for i in intermediate:
    if sortbydirs:
      dirsplit = i.split(config["sep"])
      dir = dirsplit[0] + config["sep"]
      
      if dir not in result_list:
        result_list.append(dir[:-1] if db_list(path + dir) == [] else dir)

    else:
      result_list.append(i)
  return result_list



def drop(path: str = config["sep"]):
  "drop all stored keys within a path"
  valcheck(root(path))
  
  for i in db_list(path, False, False):
    del db[msg + i]

def reference(method: str, input, path: str = config["sep"]):
  """generate a reference string under a specified method,
  one or two inputs may be required"""
  mu = method.upper()
  ref = ""
  header = config["ref"] + mu + " "
  if mu not in methods:
    raise ValueError("bad method")
  if mu == "FROM":
    ref = header + config["sep"].join(root(path)) + " " + input
  elif mu == "ENV":
    ref = header + input
  return ref


def read(key: str, path: str = config["sep"]):
        inpath = config["sep"].join(root(path))
        value = db_grab(msg + inpath + key)
        if utils.is_reference(value):
            value = value[len(config["ref"]):]
            cmd = value.split()[0]
            if cmd == "FROM":
                vpath = value.split()[1]
                vkey = value.split()[2]
                return read(vkey, vpath)
            elif cmd == "ENV":
              return os.environ[value.split()[-1]]
            
        else:
          return value