#################################################################
# Input Data
#################################################################
wt = list(map(int, input().split()))
val = list(map(int, input().split()))
W = int(input())
n = len(wt)

#################################################################
# Recursive Method
#################################################################
def unbounded_knapsack(wt, val, n, W):
    if n == 0 or W == 0:
        return 0

    if W >= wt[n-1]:
        return max(val[n-1]+unbounded_knapsack(wt, val, n, W-wt[n-1]), unbounded_knapsack(wt, val, n-1, W))

    elif W < wt[n-1]:
        return unbounded_knapsack(wt, val, n-1, W)

print(unbounded_knapsack(wt, val, n, W))