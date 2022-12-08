import aocd
rawdata = aocd.get_data(day=2, year=2022)
data = rawdata.split("\n")

scores = {'X' : 1, 'Y' : 2, 'Z' : 3}

win = { 'X' : {'A' : 3, 'B' : 0, 'C' : 6},
        'Y' : {'A' : 6, 'B' : 3, 'C' : 0},
        'Z' : {'A' : 0, 'B' : 6, 'C' : 3}}
        
lose = {'A' : 'Z', 'B' : 'X', 'C' : 'Y'}
draw = {'A' : 'X', 'B' : 'Y', 'C' : 'Z'}
winn = {'A' : 'Y', 'B' : 'Z', 'C' : 'X'}


#print(data)
score = 0
for d in data:
    a = d.split()
    t = a[0]
    s = a[1]
    action = ''
    if s == 'X':
        action = lose[t]
    elif s == 'Y':
        action = draw[t]
    elif s == 'Z':
        action = winn[t]
        
    score += scores[action] + win[action][a[0]]


myanswer = score
print(myanswer)
aocd.submit(myanswer, part='B', day=2, year=2022)