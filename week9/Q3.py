n = list(map(int, input().split()))
n.sort(reverse=True)
max = int(input())
cnt = 0
while True:
    if len(n) > 1:
        if (n[0] + n[-1] > max):
            n.remove(n[0])
            cnt += 1
        else:
            n.remove(n[0] )
            n.remove(n[-1])
            cnt += 1
    elif len(n) == 1:
        cnt += 1
        break
    else:
        break
print(cnt)
        
