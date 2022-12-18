import aocd
import helper
import numpy as np

day = 17
data = aocd.get_data(day=day, year=2022)
datatest = helper.readfile()

def part1(data):
    rocks = [[(0,0), (1,0), (2,0), (3,0)],
             [(1,0), (0,1), (1,1), (2,1), (1,2)],
             [(0,0), (1,0), (2,0), (2,1), (2,2)],
             [(0,0), (0,1), (0,2), (0,3)],
             [(0,0), (1,0), (0,1), (1,1)]]
    
    jeti = 0
    rocki = 0
    prevrocki = -1
    rock = None
    
    width = 7
    
    tower = set([(x, -1) for x in range(width)])
    for y in range(5):
        tower.add((-1, y))
        tower.add((width, y))
        
    tower_height = 0
    
    while rocki < 2022:
        jet = data[jeti % len(data)]
        if prevrocki != rocki:
            rock = list(rocks[rocki % len(rocks)])
            rock = [(x + 2, y + tower_height + 3) for x, y in rock]
            prevrocki = rocki
        rock_ = None
        if jet == '>':
            rock_ = [(x + 1, y) for x, y in rock]
        else: # jet == '<'
            rock_ = [(x - 1, y) for x, y in rock]
            
        if len(tower & set(rock_)) == 0: # jet push is allowed
            rock = list(rock_)
            if jet == '>':
               # print('right')
                pass
            else:
               # print('left')
                pass
        else:
            #print('nothing')
            pass
        
        # downward movement
        rock_ = [(x, y - 1) for x, y in rock]
        
        # collision with floor or tower during fall
        if len(tower & set(rock_)) != 0:
            for p in rock:
                tower.add(p)
                if p[1] + 1 > tower_height:
                    #print(p[1]+1)
        
                    tower_height = p[1] + 1
            rocki += 1
            #print(rock)
            tower.add((-1, tower_height))
            tower.add((width, tower_height))
        else:
            rock = list(rock_)
        
        
        jeti += 1
        
    return tower_height
    

def part2(data):
    rocks = [[(0,0), (1,0), (2,0), (3,0)],
             [(1,0), (0,1), (1,1), (2,1), (1,2)],
             [(0,0), (1,0), (2,0), (2,1), (2,2)],
             [(0,0), (0,1), (0,2), (0,3)],
             [(0,0), (1,0), (0,1), (1,1)]]
    
    jeti = 0
    rocki = 0
    prevrocki = -1
    rock = None
    
    width = 7
    
    tower = set([(x, -1) for x in range(width)])
    for y in range(5):
        tower.add((-1, y))
        tower.add((width, y))
        
    tower_height = 0
    
    cycles = set()
    cycle = []
    
    while rocki < 10000000:
        jet = data[jeti % len(data)]
        if prevrocki != rocki:
            rock = list(rocks[rocki % len(rocks)])
            rock = [(x + 2, y + tower_height + 3) for x, y in rock]
            prevrocki = rocki
            cycle = set()
            
        rock_ = None
        if jet == '>':
            rock_ = [(x + 1, y) for x, y in rock]
        else: # jet == '<'
            rock_ = [(x - 1, y) for x, y in rock]
            
        if len(tower & set(rock_)) == 0: # jet push is allowed
            rock = list(rock_)
            if jet == '>':
               # print('right')
                pass
            else:
               # print('left')
                pass
        else:
            #print('nothing')
            pass
        
        # downward movement
        rock_ = [(x, y - 1) for x, y in rock]
        
        # collision with floor or tower during fall
        if len(tower & set(rock_)) != 0:
            for p in rock:
                tower.add(p)
                cycle.add(p)
                if p[1] + 1 > tower_height:
                    #print(p[1]+1)
        
                    tower_height = p[1] + 1
            rocki += 1
            #print(rock)
            tower.add((-1, tower_height))
            tower.add((width, tower_height))
            if rocki % 5 == 0 and jeti == len(data)-1:
                print('break')
                break
        else:
            rock = list(rock_)
        
        
        jeti += 1
    
    print(1000000000000 / rocki)
    tower_height_ = tower_height * (1000000000000 // rocki)
    jeti = 0
    rocki = 1000000000000 - rocki
    
    jeti = 0
    prevrocki = -1
    rock = None
    
    width = 7
    
    tower = set([(x, -1) for x in range(width)])
    for y in range(5):
        tower.add((-1, y))
        tower.add((width, y))
        
    tower_height = 0
     
    while rocki < 1000000000000:
        jet = data[jeti % len(data)]
        if prevrocki != rocki:
            rock = list(rocks[rocki % len(rocks)])
            rock = [(x + 2, y + tower_height + 3) for x, y in rock]
            prevrocki = rocki
            
        rock_ = None
        if jet == '>':
            rock_ = [(x + 1, y) for x, y in rock]
        else: # jet == '<'
            rock_ = [(x - 1, y) for x, y in rock]
            
        if len(tower & set(rock_)) == 0: # jet push is allowed
            rock = list(rock_)
            if jet == '>':
               # print('right')
                pass
            else:
               # print('left')
                pass
        else:
            #print('nothing')
            pass
        
        # downward movement
        rock_ = [(x, y - 1) for x, y in rock]
        
        # collision with floor or tower during fall
        if len(tower & set(rock_)) != 0:
            for p in rock:
                tower.add(p)
                if p[1] + 1 > tower_height:
                    #print(p[1]+1)
        
                    tower_height = p[1] + 1
            rocki += 1
            #print(rock)
            tower.add((-1, tower_height))
            tower.add((width, tower_height))
        else:
            rock = list(rock_)
    
        
    return tower_height + tower_height_

answer_a = part1(data)
answer_b = part2(datatest)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day year=2022)
#aocd.submit(answer_b, part='B', day=day year=2022)