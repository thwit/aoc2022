import aocd
import helper
import numpy as np

day = 21
data = aocd.get_data(day=day, year=2022)
#data = helper.readfile()
data = data.split('\n')


def evaluate(monkeys, m='root'):
    
    left = monkeys[m].get('a', None)
    op = monkeys[m].get('op', None)
    right = monkeys[m].get('b', None)
    num = monkeys[m].get('n', None)
    
    #print(monkeys[m])
    
    if num is not None:
        return num
    
    if op == '+':
        return evaluate(monkeys, left) + evaluate(monkeys, right)
    if op == '-':
        return evaluate(monkeys, left) - evaluate(monkeys, right)
    if op == '*':
        return evaluate(monkeys, left) * evaluate(monkeys, right)
    if op == '/':
        return evaluate(monkeys, left) / evaluate(monkeys, right)

def part1(data):
    monkeys = {}
    
    for line in data:
        mnk, rest = line.split(': ')
        
        if any((c in rest) for c in '+-*/'):
            left, op, right = rest.split(' ')
            monkeys[mnk] = {'a': left, 'op': op, 'b': right}
        else:
            num = int(rest)
            monkeys[mnk] = {'n': num}
    
    return evaluate(monkeys)
    
def part2(data):
    monkeys = {}
    
    for line in data:
        mnk, rest = line.split(': ')
        
        if any((c in rest) for c in '+-*/'):
            left, op, right = rest.split(' ')
            monkeys[mnk] = {'a': left, 'op': op, 'b': right}
        else:
            num = int(rest)
            monkeys[mnk] = {'n': num}
    
    upper = 10000000000000000
    lower = -1000000000000
    
    b = evaluate(monkeys, monkeys['root']['b'])
    
    while True:
        k = lower + (upper - lower) // 2
        monkeys['humn']['n'] = k
        a = evaluate(monkeys, monkeys['root']['a'])
        
        if a - b == 0:
            break
        
        if a - b > 0:
            if lower == k:
                break
            lower = k
        elif a - b < 0:
            upper = 
        
    return monkeys['humn']['n']


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day, year=2022)
#aocd.submit(answer_b, part='B', day=day, year=2022)