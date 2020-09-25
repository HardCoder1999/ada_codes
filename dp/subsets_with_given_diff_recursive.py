#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
x = int(input())
n = len(ar)
sum_ = sum(ar)
s = int((sum_ - x)/2)

#################################################################
# Recursive Method
#################################################################
def subset_given_diff(ar, n, s):
    if s == 0:
        return True

    elif n == 0 and s != 0:
        return False
    
    if s >= 0:
        return subset_given_diff(ar, n-1, s-ar[n-1]) + subset_given_diff(ar, n-1, s)
    
    elif s < 0:
        return subset_given_diff(ar, n-1, s)

print(subset_given_diff(ar, n, s))