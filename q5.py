import aocd
import string
rawdata = aocd.get_data(day=5, year=2022)
stacks_input = rawdata.split('\n')[:10]
data = rawdata.split("\n")[10:]

stacks = [[] for _ in range(9)]
for boxes in stacks_input:
    for i, box in enumerate(boxes):
        if not box.isalpha():
            continue
        stacks[(i-1)//4].append(box)
    
for i in range(len(stacks)):
    stacks[i] = list(reversed(stacks[i]))

def part1(data):
    aa = 0
    for i, d in enumerate(data):
        cmds = d.split(' ')
        cmds = [int(x) for x in cmds if x.isdigit()]
        amount, frm, to = cmds
        amount = min(len(stacks[frm-1]), amount)
        #print(amount, frm, to)

        
        #amount = min(amount, len(stacks[frm-1]))
        stacks[to-1].extend(stacks[frm-1][-amount:])
        stacks[frm-1] = stacks[frm-1][:len(stacks[frm-1]) - amount]
    
def part2(data):
    aa = 0
    for i, d in enumerate(data):
        cmds = d.split(' ')
        cmds = [int(x) for x in cmds if x.isdigit()]
        amount, frm, to = cmds
        amount = min(len(stacks[frm-1]), amount)
        #print(amount, frm, to)

        
        #amount = min(amount, len(stacks[frm-1]))
        stacks[to-1].extend(reversed(stacks[frm-1][-amount:]))
        stacks[frm-1] = stacks[frm-1][:len(stacks[frm-1]) - amount]
  
myanswer = part1(data)
print()
for stack in stacks:
    print(stack[-1], end='')

#print(myanswer)
#aocd.submit(myanswer, part='A', day=5 year=2022)