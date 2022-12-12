import re
import shutil
import sys
import os

def ints(string):
    return list(map(int, re.findall(r"-?[0-9]+", string)))

def readfile():
    with open("data.txt","r") as f:
        return f.read()
    
    
if __name__ == "__main__":
    day = sys.argv[1:][0]
    fname = f'q{day}.py'
    
    if not os.path.exists(os.path.join(fname)):
        shutil.copyfile('template.py', fname)
        print(fname + ' created.')
    else:
        print(fname + ' already exists.')