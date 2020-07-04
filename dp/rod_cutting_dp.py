#################################################################
# Input Data
#################################################################
wt = list(map(int, input().split()))
val = list(map(int, input().split()))
W = int(input())
n = len(wt)

#################################################################
# Dynamic Programming Method
#################################################################
t = [[0 for j in range(W+1)] for i in range(n+1)]

for i in range(n+1):
    for j in range(W+1):
        if j >= wt[i-1]:
            t[i][j] = max(t[i-1][j-wt[i-1]], t[i-1][j])
        elif j < wt[i-1]:
            t[i][j] = t[i-1][j]

print(t[i][j]) 