#################################################################
# Input Data
#################################################################
wt = list(map(int, input().split()))
val = list(map(int, input().split()))
s = int(input())
n = len(wt)

#################################################################
# Memoized Code 
#################################################################
t = [[-1 for j in range(s+1)] for i in range(n+1)]
def knapsack_memo(wt, val, s, n, t):
    if s == 0 or n == 0:
        return 0
    if t[n][s] != -1:
        return t[n][s]

    elif s >= wt[n-1]:
        t[n][s] = max(val[n-1]+knapsack_memo(wt, val, s-wt[n-1], n-1, t), knapsack_memo(wt, val, s, n-1, t))
    
    elif s < wt[n-1]:
        t[n][s] = knapsack_memo(wt, val, s, n-1, t)

    return t[n][s]

print(knapsack_memo(wt, val, s, n, t))