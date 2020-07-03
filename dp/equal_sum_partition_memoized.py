#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
ar_sum = sum(ar)
n = len(ar)
s = ar_sum // 2
#################################################################
# Memoized Method
#################################################################
t = [[None for j in range(s+1)] for i in range(n+1)]

def equal_sum(ar, s, n, t):
    if s == 0:
        return True
    elif n == 0 and s != 0:
        return False
    
    if t[n][s] != None:
        return t[n][s]
    elif s >= ar[n-1]:
        t[n][s] = equal_sum(ar, s-ar[n-1], n-1, t) or equal_sum(ar, s, n-1, t)
    elif s < ar[n-1]:
        t[n][s] = equal_sum(ar, s, n-1, t)

    return t[n][s]


if ar_sum % 2 != 0:
    print(False)
else:
    print(equal_sum(ar, s, n, t))
