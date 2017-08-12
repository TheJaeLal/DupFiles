# DupFiles
A duplicate file checker application.

It scans the specified directory for duplicate files, and lists them if any.

# Algorithm
It calculates the md5 hash for comparing files.

# Usage
python hash-me.py <path/to/directory/to/search/for/duplicates>

If no path is supplied, it looks for duplicates in the current-directory (one containing the source file)

Add flag -0 to include Empty files in the search

eg. 

python hash-me.py <path/to/dir> -0

or

python hash-me.py -0

# Output
Checking for duplicate files in <path/to/directory>

Found 2 duplicates

'abc.txt' is a possible duplicate of 'def.txt'

'456.c' is a possible duplicate of '123.c'
