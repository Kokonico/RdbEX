# RdbEX
>Replit DataBase EXtended
><br>0.3 alpha

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

### (NOTE: does NOT support versions below 0.3.x)

in the script you would like to use RdbEX in, import it using `import rdbex`

to create a new database controller, use `dbc = rdbex.DBcontroller()`

to set a key to a value, use `dbc.set('key', 'value')`
 * _note: to set a key under a path/folder use `dbc.set('key', 'value', 'path|to|folder')`_

to delete a key for a value, use `dbc.delete('key')`
  *_note: deleting a key under a folder is the exact same as creating one._

check the official wiki for advanced documentation, such as referencing, listing, and more.