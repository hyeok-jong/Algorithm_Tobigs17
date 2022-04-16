
import sys
m,n = input().split()
m = int(m)
n = int(n)
cards = [list(input()) for i in range(m)]


def count(x, m, n):
    odd = 0
    cnt = 0
    cnt_set = set()
    for i in range(m, m + 8):
        for j in range(n, n + 8):
            if (j + odd)%2 == 0:
                cnt += (cards[i][j]=="B")
            else:
                cnt += (cards[i][j]=="R")
        odd += 1
    cnt_set.add(cnt)
    
    odd = 0
    cnt = 0
    for i in range(m, m + 8):
        for j in range(n, n + 8):
            if (j + odd)%2 == 0:
                cnt += (cards[i][j]=="R")
            else:
                cnt += (cards[i][j]=="B")
        odd += 1
    cnt_set.add(cnt)
    return cnt_set
    
    
an = 100000
for i in range(0,m-7):
    for j in range(0,n-7):
        if an > min(count(cards, i, j)):
            an = min(count(cards, i, j))
print(an)
        

    

        
