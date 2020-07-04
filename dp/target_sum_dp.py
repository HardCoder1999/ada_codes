#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
n = len(ar)
sum_ = sum(ar)
x = int(input())
s = int((sum_ - x)/2)

#################################################################
# Dynamic Programming
#################################################################
t = [[0 for j in range(s+1)] for i in range(n+1)]
for i in range(n+1):
    t[i][0] = 1

for i in range(1, n+1):
    for j in range(1, s+1):
        if j >= ar[i-1]:
            t[i][j] = t[i-1][j-ar[i-1]] + t[i-1][j]
        else:
            t[i][j] = t[i-1][j]

print(t[n][s])