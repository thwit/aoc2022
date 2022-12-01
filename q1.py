import aocd as aocd


rawdata = aocd.get_data(day=1, year=2022)
data2 = rawdata.splitlines()
data = [0 for _ in range(100000)]
i = 0
for d in data2:
    
    if d == '':
        i+= 1
    else:
        data[i] += int(d)

data.sort()
myanswer = sum(data[-3:])


#myanswer = abs(x) + abs(y)
#print(myanswer)
aocd.submit(myanswer, part='B', day=1, year=2022)