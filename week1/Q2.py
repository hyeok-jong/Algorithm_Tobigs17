import sys

n = sys.stdin.readline()
n = int(n)
path = sys.stdin.readline().split()

location = {'col':1, 'row':1}
location

for i in path:
    if i == "R" and location['row'] < n:
        location['row']+=1
    if i == "L" and location['row'] > 1:
        location['row']-=1
    if i == "D" and location['col'] < n:
        location['col']+=1
    if i == "U" and location['col'] > 1:
        location['col']-=1   
print(location['col'],location['row'])
