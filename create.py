# Creates programs based on:
# 1. Base programs in the templates folder
# 2. Or calls the latest boilerplates from the interwebs

# imports
import sys
import os.path
# import requests
from subprocess import call

# Requirements -----------------------------------------------------------------
# python_version = sys.version
# if python_version < 2:
# 	print 'Please Update your Python Version'

# Functions --------------------------------------------------------------------
def file_exists(path):
	return os.path.isfile(path)

def file_does_not_exist(path):
	if os.path.isfile(path):
		return False
	return True

def clone_file(read_path,write_path):
	with open(read_path, 'r') as fr:
		with open(write_path, 'w') as fw:
			fw.write(fr.read())
			return True
		return False
	return False

def open_atom(file_path):
	call([
		'atom',
		file_path,
	])

def create(r_directory,extention,attempt=0):
	r_path = './templates/' + r_directory + '/base.' + extention
	w_path = './base.' + extention
	if attempt:
		w_path = w_path.replace('./base','./base' + str(attempt))
	if file_exists(r_path) and file_does_not_exist(w_path):
		if clone_file(r_path,w_path):
			open_atom(w_path)
		else:
			print 'Error: Cound not clone file.'
	elif attempt < 1000:
		create('html','html',attempt+1)
	else:
		print 'Sorry, we limit you to 1000 files in a single directory!'

# Mapping ----------------------------------------------------------------------
html = ['html','html5']

# Program ----------------------------------------------------------------------
language = sys.argv[1]

if language in html:
	create('html','html')
else:
	print 'sorry bro'
