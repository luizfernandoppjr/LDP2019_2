#Problema 1
import os
def mkdir(directory): 
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def touch(file):
    if not os.path.exists(file):
        open(file, "w").close()

mkdir("dir1/dir2/dir3")
mkdir("dir1/dir4/dir5")

touch("dir1/dir2/dir3/file.txt")

#import os 
os.rename("dir1/dir4/dir5/file.txt", "dir1/dir2/dir3/file2.txt")