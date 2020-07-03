#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
s = int(input())
n = len(ar)

#################################################################
# Memoized Solution
#################################################################
t = [[None for j in range(s+1)] for i in range(n+1)]

def subset_sum(ar, s, n, t):
    if s == 0:
        return True

    elif n == 0 and s != 0:
        return False

    if t[n][s] != None:
        return t[n][s]

    if s >= ar[n-1]:
        t[n][s] = subset_sum(ar, s-ar[n-1], n-1, t) or subset_sum(ar, s, n-1, t)

    elif s < ar[n-1]:
        t[n][s] = subset_sum(ar, s, n-1, t)

    return t[n][s]


print(subset_sum(ar, s, n, t))