import sys

U,D,H = sys.stdin.readline().split()

U = int(U)
D = int(D)
H = int(H)
k = (H-D)/(U-D)
print(int(k) if k == int(k) else int(k) + 1)
