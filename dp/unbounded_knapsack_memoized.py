#################################################################
# Input Data
#################################################################
wt = list(map(int, input().split()))
val = list(map(int, input().split()))
W = int(input())
n = len(wt)

#################################################################
# Memoization Method
#################################################################
t = [[-1 for j in range(W+1)] for i in range(n+1)]

def unbounded_knapsack(wt, val, n, W, t):
    if n == 0 or W == 0:
        return 0

    if t[n][W] != -1:
        return t[n][W]

    if W >= wt[n-1]:
        t[n][W] = max(val[n-1] + unbounded_knapsack(wt, val, n, W-wt[n-1], t) , unbounded_knapsack(wt, val, n-1, W, t))

    elif W < wt[n-1]:
        t[n][W] = unbounded_knapsack(wt, val, n-1, W, t)

    return t[n][W]

print(unbounded_knapsack(wt, val, n, W, t))
