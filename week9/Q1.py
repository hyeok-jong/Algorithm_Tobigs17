n,m = map(int,input().split())
nums = [int(input())  for _ in range(n)]
nums.reverse()


cnt = 0
left = m
for i in nums:
    while left >= i:
        left -= i
        cnt += 1
        
print(cnt)
        
