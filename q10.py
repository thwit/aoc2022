import aocd
import helper
import numpy as np

day = 10
data = aocd.get_data(day=day, year=2022)
data = data.split('\n')

def part1(data):
    x = 1
    sums = []
    
    cycle = 0
    for cmd in data:
        to_cycle = 1 if 'noop' in cmd else 2
        
        for _ in range(to_cycle):
            cycle += 1
            if (cycle+20) % 40 == 0:
                sums.append(cycle*x)
        
        if 'addx' in cmd:
            x += int(cmd.split()[1])
            
    return sum(sums)
    
def part2(data):
    x = 1
    cycle = 0
    print('.', end='')
    for cmd in data:
        to_cycle = 1 if 'noop' in cmd else 2
        for _ in range(to_cycle):
            cycle += 1
            if cycle % 40 == 0:
                print()
            if (cycle-1) % 40 in [x-1, x, x+1]:
                print('#', end='')
            else:
                print('.', end='')
        
        if 'addx' in cmd:
            x += int(cmd.split()[1])


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day year=2022)
#aocd.submit(answer_b, part='B', day=day year=2022)