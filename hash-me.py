import hashlib
import os,sys

if len(sys.argv)==1:
	mydir = os.getcwd()
else:
	mydir = sys.argv[1]

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

file_list = os.listdir(mydir)

seen_files = dict()
duplicate = dict()

for f in file_list:	
	Fname = os.path.join(mydir,f)
	#Ignore directories
	if os.path.isdir(Fname):
		continue
	#Ignore Linux-Backup files
	if f.endswith('~'):
		continue
	#Ignore Empty Files
	if os.path.getsize(Fname)==0:
		continue
	Fhash = md5(Fname)
	if Fhash in seen_files:
		duplicate[seen_files[Fhash]] = f
	else:
		seen_files[Fhash] = f

print('Checking for duplicate...')
for f in duplicate:
	print(duplicate[f],'is a possible duplicate of',f)

