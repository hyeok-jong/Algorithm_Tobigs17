n = int(input())

doc = [0]*(n*2)
for i in range(2, n+1):
    doc[i] = doc[i-1] + 1
    if i % 3 == 0:
        doc[i] = min(doc[i], doc[i//3] + 1)
    if i % 2 == 0:
        doc[i] = min(doc[i], doc[i//2] + 1)
print(doc[n])
