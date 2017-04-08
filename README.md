# Creator
A program that creates programs

## What Creator Does
1. Creates a program in your current directory based off the language you want to work with. Will add a number to the end of it if filename (base) already exists.
2. Opens your program for editing

## Installation

### Requirements
1. Python
2. Python Plugins
3. Install Alias (#Alius)

### Alias
Add an alias to your .bash_profile to copy templates over.

Example (needs to be updated):
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
