import aocd
import helper
import numpy as np

day = 11
data = aocd.get_data(day=day, year=2022)
monkeys = data.split('\n\n')

ops = [ lambda x: x * 17,
        lambda x: x + 8,
        lambda x: x + 6,
        lambda x: x * 19,
        lambda x: x + 7,
        lambda x: x * x,
        lambda x: x + 1,
        lambda x: x + 2 ]

class Monkey:
    def __init__(self, items, operation, div, divtrue, divfalse):
        self.items = items
        self.operation = operation
        self.div = div
        self.divtrue = divtrue
        self.divfalse = divfalse
        self.biz = 0
        
    
    def test(self, num):
        if num % self.div == 0:
            return self.divtrue
        else:
            return self.divfalse

def get_monkeys(monkeys):
    mnks = []
    for j, monkey in enumerate(monkeys):
        items = []
        div = None
        totrue = None
        tofalse = None
        
        for i, line in enumerate(monkey.split('\n')[1:]):
            if i == 0:
                items = helper.ints(line)
            if i == 1:
                continue
            if i == 2:
                div = helper.ints(line)[0]
            if i == 3:
                totrue = helper.ints(line)[0]
            if i == 4:
                tofalse = helper.ints(line)[0]
        
        mnks.append(Monkey(items, ops[j], div, totrue, tofalse))
    return mnks

def part1(mnks):
    for _ in range(20):
        for mnk in mnks:
            for _ in range(len(mnk.items)):
                mnk.biz += 1
                item = mnk.items[0]
                mnk.items.pop(0)
                
                item = mnk.operation(item)
                item = item // 3
                
                to_mnk = mnk.test(item)
                mnks[to_mnk].items.append(item)
        
    bizz = sorted([mnk.biz for mnk in mnks], reverse=False)
    print(bizz)
    return bizz[-1] * bizz[-2]
    
def part2(mnks):
    comp = 1
    for mnk in mnks:
        comp *= mnk.div

    for _ in range(10000):
        for mnk in mnks:
            for _ in range(len(mnk.items)):
                mnk.biz += 1
                item = mnk.items[0]
                mnk.items.pop(0)
                
                item = mnk.operation(item)
                item = item % comp
                
                to_mnk = mnk.test(item)
                mnks[to_mnk].items.append(item)
        
    bizz = sorted([mnk.biz for mnk in mnks], reverse=False)
    print(bizz)
    return bizz[-1] * bizz[-2]
    
mnks = get_monkeys(monkeys)
answer_a = part1(mnks)
answer_b = part2(mnks)