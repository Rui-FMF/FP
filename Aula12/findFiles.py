import os

def printDirFiles(d):
    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path):
            ftype = "FILE"
        elif os.path.isdir(path):
            ftype = "DIR"
        else:
            ftype = "?"
        print(ftype, path)

printDirFiles("..")


def findFiles(path, ext):
    ...


# Test findFiles:
lst = findFiles(".", ".py")
print(lst)
assert isinstance(lst, list)

lst = findFiles("..", ".csv")
print(lst)

