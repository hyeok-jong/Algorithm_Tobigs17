import sys

n,m = sys.stdin.readline().split()
n = int(n)
m = int(m)
cards = [list(map(int,sys.stdin.readline().split())) for i in range(n)]


a = -1
for i in cards:
    min_n = min(i)
    if min_n > a:
        a = min_n
print(a)
