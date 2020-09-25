#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
n = len(ar)
s = sum(ar)

#################################################################
# Dynamic Programming method
#################################################################
t = [[False for j in range(s+1)] for i in range(n+1)]
for i in range(n+1):
    t[i][0] = True

for i in range(1, n+1):
    for j in range(1, s+1):
        if j >= ar[i-1]:
            t[i][j] = t[i-1][j-ar[i-1]] or t[i-1][j]
        elif j < ar[i-1]:
            t[i][j] = t[i-1][j]

for j in range(int(s/2), -1, -1):
    if t[n][j] == True:
        diff = s-2*j
        break

print(diff)