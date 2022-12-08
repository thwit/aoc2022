import aocd
import string
rawdata = aocd.get_data(day=4, year=2022)
data = rawdata.split("\n")
#print(data)

def part1(data):
    aa = 0
    for d in data:
        a, b = d.split(',')
        print(a,b)
        l1 = int(a[:a.index('-')])
        u1 = int(a[a.index('-')+1:])
        l2 = int(b[:b.index('-')])
        u2 = int(b[b.index('-')+1:])
        if l1 <= l2 and u1 >= u2:
            aa+=1
        elif l2 <= l1 and u2 >= u1:
            aa+=1
    return aa
        
        
    
def part2(data):
    aa = 0
    for d in data:
        a, b = d.split(',')
        print(a,b)
        l1 = int(a[:a.index('-')])
        u1 = int(a[a.index('-')+1:])
        l2 = int(b[:b.index('-')])
        u2 = int(b[b.index('-')+1:])
        if l1 <= u2 and u1 >= l2:
            aa+=1
        elif l2 <= u1 and u2 >= l1:
            aa+=1
    return aa
    
myanswer = part2(data)
print(myanswer)
#aocd.submit(myanswer, part='A', day=4, year=2022)