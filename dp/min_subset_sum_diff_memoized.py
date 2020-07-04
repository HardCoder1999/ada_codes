#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
n = len(ar)
s = sum(ar)

#################################################################
# Memoized Method
#################################################################
t = [[-1 for j in range(s+1)] for i in range(n+1)]

# there are some mistakes in the code, need some recheck.
def min_subset_val(ar, n, s, sumCalculated):
    if n == 0:
        return abs((s-sumCalculated)-sumCalculated)
    
    if t[n][s] != -1:
        return t[n][s]
    
    t[n][s] = min(min_subset_val(ar, n-1, s, sumCalculated+ar[n-1]), min_subset_val(ar, n-1, s, sumCalculated))
    return t[n][s]

print(min_subset_val(ar, n, s, 0))
