# RdbEX
## Replit DataBase EXtended

Replit database extended is a package designed to expand the abilities of the default replit database.

it adds things such as:
<br>
**emulated folders**
<br>
**ease of access**
<br>
**value sharing**
<br>
**safe secret storage**
<br>
*and much more...*

## how to use: a basic rundown

after installing the package, import using <code>import RdbEX</code>.

to create a new key in the root directory, use <code> RdbEX.create("keyname")</code>.

to delete a key, use <code> RdbEX.delete("keyname")</code>.

to create a new key within a folder, use <code> RdbEX.create("keyname", "folderA")</code>. (same thing for deleting keys within folders)

to create keys within nested folders, use <code> RdbEX.create("keyname", "folderA|folderB")</code>. (same thing for deleting keys within folders)

to list keys and list keys within a folder(s), use <code> RdbEX.list("folderA|folderB (optional)")</code>.

and to drop your database (with an optional path), use <code> RdbEX.drop("folderpath (optional)")</code>

keep in mind that by default, "|" is the spacing character for folders, this can be changed in RdbEX -> config.py

(please note that this is not full documentation, and it will be coming soon.)