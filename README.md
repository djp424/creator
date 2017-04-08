# Creator Overview
1. Creates a program in your current directory based off the language you want to work with. Will add a number to the end of the filename (base) if it already exists.
2. Opens your program in your editor.

## Installation

### Requirements
1. Python
2. Python Plugins (TODO: needs to be updated)
3. Update Alias

### Alias
Open your .bash_profile and add the following line to it (TODO: needs to be updated):
```
alias create='cp /Users/dparsons/Code/creator/templates/base.py .; atom .'
```

Note: Make sure to update your .bash_profile with "source ~/.bash_profile" when making changes

## How To Use
1. Go to a directory you want to start your test in via your terminal.
2. Type in "create html" to setup a base html file.

## To Do
* Add support for non-atom editors
* Add option to override base templates
* Add more bases
  * PHP
  * JSON
  * Ruby
* Add in complicated bases
  * node.js
  * node.js + express
  * WordPress
  * Drupal
