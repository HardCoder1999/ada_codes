#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
n = len(ar)
sum_ = sum(ar)
x = int(input())
s = int((sum_ - x)/2)

#################################################################
# Memoize Data
#################################################################
t = [[-1 for j in range(s+1)] for i in range(n+1)]

def subset_given_diff(ar, n, s):
    if s == 0:
        return True
    
    elif n == 0 and s != 0:
        return False
    
    if t[n][s] != -1:
        return t[n][s]
    
    if s >= ar[n-1]:
        t[n][s] = subset_given_diff(ar, n-1, s-ar[n-1]) + subset_given_diff(ar, n-1, s)
    elif s < ar[n-1]:
        t[n][s] = subset_given_diff(ar, n-1, s)

    return t[n][s]


print(subset_given_diff(ar, n, s))
