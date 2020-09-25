#################################################################
# Input Data
#################################################################
wt = list(map(int, input().split()))
val = list(map(int, input().split()))
s = int(input())
n = len(wt)

#################################################################
# Recursive Code 
#################################################################
def knapsack_(wt, val, s, n):
	if s == 0 or n == 0:
		return 0
	else:
		if s >= wt[n-1]:
			return max(val[n-1]+knapsack_(wt, val, s-wt[n-1], n-1), knapsack_(wt, val, s, n-1))
		elif s < wt[n-1]:
			return knapsack_(wt, val, s, n-1)

print(knapsack_(wt, val, s, n))
