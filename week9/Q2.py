n = int(input())
times = [list(map(int, input().split())) for i in range(n)]
times = sorted(times, key=lambda x: (x[1], x[0]))

cnt = 0
last = -1
for start, end in times:
    if start >= last:
        last = end
        cnt += 1
        
print(cnt)
