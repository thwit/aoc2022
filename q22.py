import aocd
import helper
import numpy as np

day = 22
data = aocd.get_data(day=day, year=2022)
data = helper.readfile()
data = data.split('\n')

def part1(data):
    field = []
    for line in data[:-1]:
        field.append(list(line))
        
    cmds = data[-1]
    moves = helper.ints(cmds)
    rotat = [x for x in cmds if x == 'R' or x == 'L']
    
    cmds = []
    for i in range(len(moves) + len(rotat)):
        if i % 2 == 0:
            cmds.append(moves[0])
            moves.pop(0)
        else:
            cmds.append(rotat[0])
            rotat.pop(0)
    
    pos = None
    
    for c in range(len(field[0])):
        if c == '.':
            pos = (0, c)
    
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    facing = 0
    for cmd in cmds:
        match cmd:
            case int():
                n = cmd
                while n > 0:
                    d = dirs[facing % 4]
                    pos = (pos[0] + d[0], pos[1] + d[1])
                    if field[pos[0]][pos[1]] == ' ' and d[0] == 1:
                        pos 
                        
                        
                
            case str():
                if cmd == 'R':
                    facing += 1
                else:
                    facing -= 1
        
    
    
    
def part2(data):
    pass


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day, year=2022)
#aocd.submit(answer_b, part='B', day=day, year=2022)