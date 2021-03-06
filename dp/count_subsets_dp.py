#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
s = int(input())
n = len(ar)

#################################################################
# Dynamic Programming Method
#################################################################
t = [[0 for j in range(s+1)] for i in range(n+1)]
for i in range(n+1):
    t[i][0] = 1

for i in range(1, n+1):
    for j in range(1, s+1):
        if j >= ar[i-1]:
            t[i][j] = t[i-1][j-ar[i-1]] + t[i-1][j]
        elif j < ar[i-1]:
            t[i][j] = t[i-1][j]

print(t[n][s])