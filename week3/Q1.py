import sys
from itertools import combinations

n,m = sys.stdin.readline().split()
n = int(n)
m = int(m)
numbers = list(map(int,sys.stdin.readline().split())) 
a = set()

for i in combinations(numbers, 3):
    sum = i[0] + i[1] + i[2]
    a.add(sum)
a = list(a)

print([a for a in a if a <= m][-1])
