n = int(input())

doc = []

for i in range(n):
    doc.append(int(input()))

d = [0]*n

d[0] = doc[0]
if n > 1:
    d[1] = doc[0]+doc[1]

if n > 2:
    d[2] = max(doc[2]+doc[1], doc[2]+doc[0], d[1])

for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+doc[i-1]+doc[i], d[i-2]+doc[i])

print(d[n-1])
