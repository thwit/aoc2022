import aocd
import re
import numpy as np

def ints(string):
    return [*map(int, re.findall(r'\d+', string))]
    
class Node:
    def __init__(self, name, parent = None):
        self.x = 'Hello'
        self.parent = parent
        self.children = []
        self.name = name
        self.size = 0
        
    def compute_folder_size(self):
        if len(self.children) == 0:
            return self.size
        
        for child in self.children:
            self.size += child.compute_folder_size()
        
        return self.size
        
    def get_total_size_under_crit(self, crit):
        if len(self.children) == 0:
            return 0
            
        size = self.size if self.size <= crit else 0
        
        for child in self.children:
            sz = child.get_total_size_under_crit(crit)
            size += sz
            
        return size
        
    def get_minimum_size_over_crit(self, crit, delsize=np.inf):
        if len(self.children) == 0:
            return delsize
        
        if self.size >= crit and self.size < delsize:
            delsize = self.size
        
        for child in self.children:
            dsz = child.get_minimum_size_over_crit(crit, delsize)
            if dsz < delsize:
                delsize = dsz
        return delsize
        
def gen_directory(data):
    node = Node('/')
    basenode = node
    i = 0
    while i < len(data):
        if i == 0:
            i += 1
            continue
            
        cmd = data[i]
        
        if cmd[0] == '$':
            cmd = cmd[2:]
            
        if cmd[0] == 'c': # cd
            name = cmd.split()[1]
            if name == '/': # base folder
                node = basenode
            elif name == '..':
                node = node.parent
            else:
                node = next(folder for folder in node.children if folder.name == name)
            
            i += 1
            continue
        
        elif cmd[0] == 'l': # ls
            i+=1
            cmd = data[i]
            while cmd[0] != '$': # while not a command (aka we're checking what files/folders is children of the current folder)
                n = Node(cmd.split()[1], node)
                n.parent = node
                
                if cmd[0] != 'd': # not a directory (aka it's a file)
                    n.size = int(cmd.split()[0])
                node.children.append(n)
                
                i += 1
                if i >= len(data):
                    break
                cmd = data[i]
            continue
    return basenode

data = aocd.get_data(day=7, year=2022)
data = data.split('\n')

def part1(data):
    root = gen_directory(data)
    root.compute_folder_size()
    
    print(basenode.get_total_size_under_crit(100000)) 
       
def part1(data):
    root = gen_directory(data)
    root.compute_folder_size()
    
    crit =  30000000 - (70000000 - basenode.size)    
    print(basenode.get_minimum_size_over_crit(crit))   
       


#aocd.submit(myanswer, part='A', day=7 year=2022)