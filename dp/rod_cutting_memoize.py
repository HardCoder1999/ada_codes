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
t = [[0 for j in range(W+1)] for i in range(n+1)]
def rod_cutting():