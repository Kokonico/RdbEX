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

### (NOTE: does NOT support versions below 0.1.2)

after installing the package, import using <code>import rdbex</code>.

to create a new key in the root directory, use <code> rdbex.set("keyname")</code>.

to delete a key, use <code> rdbex.delete("keyname")</code>.

to create a new key within a folder, use <code> rdbex.set("keyname", "folderA")</code>. (same thing for deleting keys within folders)

to create keys within nested folders, use <code> rdbex.set("keyname", "folderA|folderB")</code>. (same thing for deleting keys within folders)

to list keys and list keys within a folder(s), use <code> rdbex.list("folderA|folderB (optional)")</code>.

and to drop your database (with an optional path), use <code> rdbex.drop("folderpath (optional)")</code>

### key sharing

to share a key with another value, use <code>rdbex.reference("FROM", "key", "path (optional)"</code> in the <code>value</code> section of <code>rdbex.set()</code>

### secret storage

to safely store replit secrets within your database, use <code>rdbex.reference("SECRET", "secret name")</code> in the <code>value</code> section of <code>rdbex.set()</code>
<br>
<br>
<br>
<sub>*keep in mind that by default, "|" is the spacing character for folders, this can be changed in rdbex -> config.py*

<sub>*this is not full documentation, and it will be coming soon.*

<sub>*converting databases is currently not implemented, but might happen in the future.*