n = int(input())
nums = [list(map(int, input().split()))  for _ in range(n)]

def pool(list_):
    new_ = []
    n = len(list_)
    for i in range(int(n/2)):
        new__ = []
        for j in range(int(n/2)):
            a = list_[2*i][2*j:2*j+2]+list_[2*i+1][2*j:2*j+2]
            a.sort()

            new__.append(a[-2])
        new_.append(new__)
    return(new_)



while True:
    nums = pool(nums)
    if len(nums) == 1:
        break
print(nums[0][0])

       
