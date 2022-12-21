import aocd
import helper
import numpy as np

day = 20
data = aocd.get_data(day=day, year=2022)
#data = helper.readfile()
data = data.replace('\n', ' ')

def part1(data):
    nums = helper.ints(data)
    #nums = [-1, 0, 0]
    
    nums = [(x, i) for i, x in enumerate(nums)]
    
    orig = list(nums)
    
    for x, i in orig:
        if x == 0:
            continue
        frm = nums.index((x, i))
        to = (frm + x) % (len(nums) - 1)
        
        nums.remove((x, i))
        nums.insert(to, (x,i))
            
        
    nums = [n for n, _ in nums]
    zero_idx = nums.index(0)
    
    
    return nums[(zero_idx + 1000) % len(nums)] + nums[(zero_idx + 2000) % len(nums)] + nums[(zero_idx + 3000) % len(nums)]
    
    
def part2(data):
    nums = helper.ints(data)
    
    deckey = 811589153
    
    nums = [(x * deckey, i) for i, x in enumerate(nums)]
    
    orig = list(nums)
    for _ in range(10):
        for x, i in orig:
            if x == 0:
                continue
            frm = nums.index((x, i))
            to = (frm + x) % (len(nums) - 1)
            
            nums.remove((x, i))
            nums.insert(to, (x,i))
            
    zero_idx = nums.index(0)
    return nums[(zero_idx + 1000) % len(nums)] + nums[(zero_idx + 2000) % len(nums)] + nums[(zero_idx + 3000) % len(nums)]


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day, year=2022)
#aocd.submit(answer_b, part='B', day=day, year=2022)