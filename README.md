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

### (NOTE: does NOT support versions below 0.2)

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

to safely store replit secrets and os environment variables within your database, use <code>rdbex.reference("ENV", "variable name")</code> in the <code>value</code> section of <code>rdbex.set()</code>

## Recovery.

### warning!

to repair anything without reinstalling the package, you need to make sure the "recovery.py" and "__internal/_recovery.py" files are accessible.
<br>
<br>
if you delete a required file from the package or the package gets corrupted and if fails to load on import, you will get an ImportError that says *"The package has been installed incorrectly and/or has been corrupted. please reinstall the package."*, to fix this, just uninstall & reinstall the package using the package manager of your choice.

if the database is corrupted, you will get an ImportError saying *"critical damage to rdbex detected. a repair has been ran, please restart. if the error persists, use "from rdbex import recovery" and run recovery.rebuild() to attempt to fix the issue"*, before doing anything, try rerunning the code, as it attempts to repair the database. if the error still persists, run <code>from rdbex import recovery</code>. after importing recovery, run <code>recovery.rebuild()</code> to completely rebuild the database metadata. 
<br>
***this WILL wipe ALL user-set config, but NOT the db***

<br>
<br>
<br>
<sub>*keep in mind that by default, "|" is the spacing character for folders, this can be changed via the <code>configure()</code> command in utils*

<sub>*this is not full documentation, and it will be coming soon.*

<sub>*converting databases is currently not implemented, but might happen in the future.*