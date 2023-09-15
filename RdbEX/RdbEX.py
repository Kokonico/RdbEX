from replit import db

# internal functions

def __genpath__(path, key):
  if  not path.startswith("|"):
    return "|" + path + key
  else:
    return path
    
def create(key, value, path):
  pathg = __genpath__(path, key)
  db[str(pathg)] = value
  return db[str(pathg)]

def delete(key, path):
  pathg = __genpath__(path, key)
  if pathg in db:
    del db[pathg]
  else:
    raise FileNotFoundError('No stored key under "' + pathg + '"')

def list(path):
  return db.keys()