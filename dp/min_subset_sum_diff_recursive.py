#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
n = len(ar)
s = sum(ar)

#################################################################
# Recursive Method
#################################################################


def min_subset_diff(ar, n, s, sumCalculated):
    if n == 0:
        return abs((s - sumCalculated) - sumCalculated)
    else:
        return min(min_subset_diff(ar, n-1, s, sumCalculated+ar[n-1]), min_subset_diff(ar, n-1, s, sumCalculated))


print(min_subset_diff(ar, n, s, 0))
