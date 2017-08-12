#!/usr/bin/python3

from __future__ import print_function

import hashlib
import os,sys


def handle_command_line_args():
	IncludeEmpty = False
	mydir = ''

	#Only 1 agrument
	if len(sys.argv)==1:
		mydir = os.getcwd()

	#More than 1 arguments..
	elif '-0' in sys.argv:
		IncludeEmpty = True
		#Check if 3 arguments are passed
		if len(sys.argv)==3:
			#Is '-0' the 2nd argument?
			if sys.argv[1] == '-0':
				mydir = sys.argv[2]
			#'-0' the 3rd/last argument?
			else:
				mydir = sys.argv[1]

		#Only 2 arguments, no directory specified
		else:
			mydir = os.getcwd()
	#More than 1 arguments but no '-0'
	else:
		mydir = sys.argv[1]

	return mydir,IncludeEmpty

def md5(fname):
    hash_md5 = hashlib.md5()

    #Open the file
    with open(fname, "rb") as f:
        #Read data in chunks of '4096' bytes
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def find_duplicate(mydir,IncludeEmpty):
	#List all the file_names in the specified directory
	file_list = os.listdir(mydir)

	#Keep a dictionary/hashtable of all seen and duplicate files
	seen_files = dict()
	duplicate = dict()

	for f in file_list:	
		#Get the complete path of file
		Fname = os.path.join(mydir,f)
		#Ignore directories
		if os.path.isdir(Fname):
			continue
		#Ignore Linux-Backup files
		if f.endswith('~'):
			continue
		#Ignore Empty Files
		if os.path.getsize(Fname)==0 and not IncludeEmpty:
			continue
		#Calculate hash
		Fhash = md5(Fname)

		if Fhash in seen_files:
			duplicate[seen_files[Fhash]] = f
		else:
			seen_files[Fhash] = f

	return duplicate

def display(duplicate,mydir):
	print('Checking for duplicate files in',mydir)
	if duplicate:
		print('Found',len(duplicate),'duplicates')
		for f in duplicate:
			print("'{}' is a possible duplicate of '{}'".format(duplicate[f],f))
	else:
		print('None Found!')		


def main():

	mydir,IncludeEmpty = handle_command_line_args()

	duplicate_files = find_duplicate(mydir,IncludeEmpty)

	display(duplicate_files,mydir)

if __name__=='__main__':
	main()
