import os
from time import sleep

class DirectoryWalker:
    # a forward iterator that traverses a directory tree

    def __init__(self, directory):
        self.stack = [directory]
        self.files = []
        self.index = 0

    def __getitem__(self, index):
        while 1:
            try:
                file = self.files[self.index]
                self.index = self.index + 1
            except IndexError:
                # pop next directory from stack
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.index = 0
            else:
                # got a filename
                fullname = os.path.join(self.directory, file)
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    if ".git" not in fullname and "node_modules" not in fullname:
                        self.stack.append(fullname)
                return fullname

def commit(filename):
    os.system('git add "' +filename +'"')
    os.system('git commit --allow-empty -m "add ' + filename + '"')

def push():    
    os.system('git push origin main')

def main():
    directory = os.path.abspath('.') + "\\"
    for file in DirectoryWalker(os.path.abspath('.')):
        file = file.replace(directory,"")
        commit(file)

    push()

if __name__=='__main__':
    main()