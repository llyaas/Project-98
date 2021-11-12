# A = contents of file 1
# B = contents of file 2

# file1 = content of file A
# file2 = content of file B

# readLines
# open
# read
# write
# input
#function definition to swap data between 2 files
def swapFileData():
    file1Path = input("enter file1 name/Path: ")
    file2Path = input("enter file2 name/Path: ")

    with open(file1Path, 'r') as tempPlace1:
        dataofFile1 = tempPlace1.read()

    with open(file2Path, 'r') as tempPlace2:
        dataofFile2 = tempPlace2.read()

    with open(file1Path, 'w') as tempPlace1:
        tempPlace1.write(dataofFile2)

    with open(file2Path, 'w') as tempPlace2:
        tempPlace2.write(dataofFile1)

#functin call to swap data between 2 files
swapFileData()