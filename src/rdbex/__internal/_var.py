from replit import db

from . import _recovery

config_def = _recovery.config_def

methods = [
  "FROM",
  "ENV"
]

protected_header = _recovery.protected_header

meta = db[protected_header + "rdbexmeta"]

config = meta["config"]

ban = ["#", " ", "[", "]", "{", "}", "(", ")", ">", "<", config["sep"]] + list(config["banned_chars"])

msg = config["msg"] + "#"