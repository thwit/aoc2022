import re
import shutil
import sys
import os

def ints(string):
    return [*map(int, re.findall(r'\d+', string))]
    
    
    
if __name__ == "__main__":
    day = sys.argv[1:][0]
    fname = f'q{day}.py'
    
    if not os.path.exists(os.path.join(fname)):
        shutil.copyfile('template.py', fname)
        print(fname + ' created.')
    else:
        print(fname + ' already exists.')