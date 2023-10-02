from replit import db

from RdbEX import config


# internal functions
def root(inpath):
  newpath = inpath
  if inpath[0] != config.sep:
    newpath = config.sep + inpath
  if newpath[len(newpath) - 1] != config.sep:
    newpath = newpath + config.sep
  return newpath.split(config.sep)
# public functions
    
def create(key: str, value, path: str = config.sep):
  inpath = config.sep.join(root(path))
  db[inpath + key] = value

def delete(key: str, path: str = config.sep):
  inpath = config.sep.join(root(path))
  del db[inpath + key]
  
def list(path: str = config.sep, removeprefix: bool = True, sortbydirs: bool = False):
  "list all keys within a path"
  prefix = config.sep.join(root(path))
  selected_keys = db.prefix(prefix)
  result_list = []
  intermediate=[]
  for i in selected_keys:
    if removeprefix:
      intermediate.append(i.removeprefix(prefix))
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
  
  for i in list(path, False):
    del db[i]