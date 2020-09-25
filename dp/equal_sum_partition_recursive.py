#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
ar_sum = sum(ar)
n = len(ar)

#################################################################
# Recursive Solution
#################################################################

def subset_sum(ar, s, n):
    if s == 0:
        return True
    elif n == 0 and s != 0:
        return False
    else:
        if s >= ar[n-1]:
            return subset_sum(ar, s-ar[n-1], n-1) or subset_sum(ar, s, n-1)
        elif s < ar[n-1]:
            return subset_sum(ar, s, n-1)

if ar_sum % 2 != 0:
    print(False)
else:
    s = ar_sum // 2
    print(subset_sum(ar, s, n))
