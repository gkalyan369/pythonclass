import os, sys, os.path, subprocess, glob

# Check if file/path exists
print(os.path.exists("C:\\Users\\TrgDev\\PycharmProjects\\TrainingDemo\\JPMC\\sample.txt"))

# Path components of a file
names = os.path.split("C:\\Users\\TrgDev\\PycharmProjects\\TrainingDemo\\JPMC\\sample.txt")
print(names)

# Build paths using path seperator for easy porting
path_comp = ["C:", "Users", "TrgDev", "PycharmProjects", "TrainingDemo", "JPMC", "sample.txt"]
file_path = os.path.sep.join(path_comp)



# Rename files
os.rename("sample_file.txt", "sample.txt")
os.remove("dataFile.txt")
os.mkdir("subDir")
os.chdir("Day2")
print(os.getcwd())
os.rmdir("subDir")

### fileinput
# for processing contents of multiple files as a stream of lines
import fileinput

file_names = ['dataFile.txt', 'sample.txt']
for line in fileinput.input(file_names):
    print("{}. line no {} of file {}: {}".format(fileinput.lineno(), fileinput.filelineno(), fileinput.filename(), line), end='')


# skip files while processing based on conditions
with fileinput.input(files=file_names) as f:
    for line in f:
        print(fileinput.filelineno(), line, end='')
        if (fileinput.filename() == 'dataFile.txt' and fileinput.isfirstline()):
            fileinput.nextfile()
            

### stat
from stat import *

def walktree(top, processFile):
    '''recursively descend the directory tree rooted at top,
       process each regular file through a function call'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            print('Contents of directory: ', pathname)
            walktree(pathname, processFile)
        elif S_ISREG(mode):
            # It's a file, print the filename
            # or for further processing, call a function
            processFile(pathname)

def processFile(pathname):
    print(pathname)

walktree('D:\Training\Python\PycharmProjects\TrainingDemo\JPMC', processFile)


### filecmp
import filecmp
filecmp.cmp('./dataFile.txt', './Day1/datafile.txt', shallow=False)

# returns the file names as a tuple of three lists - match, mismatch, error
result = filecmp.cmpfiles('.', './Day1/', ['datafile.txt'], shallow=False)

import difflib
d = difflib.context_diff(open('./dataFile.txt').readlines(), open('./Day1/datafile.txt').readlines())
for l in d:
    print(l)

### dircmp
d = filecmp.dircmp('.', './Day1/')
d.report()
d.left
d.common
d.common_dirs
d.left_only

### zipfile and tarfile
import zipfile
z = zipfile.ZipFile('test.zip', 'w')
z.write('./Day1/dataFile.txt')
z.close()

z = zipfile.ZipFile('test.zip')
z.namelist()
z.close()


with zipfile.ZipFile('test.zip') as z:
    names = z.namelist()
    with z.open(names[0]) as myfile:
        print(myfile.read())


# File search
names = list(glob.glob('C:\\Windows\\System32\\*.exe'))
print(names)


# Execute a sub process
subprocess.run("C:\\Windows\\System32\\Notepad.exe")
