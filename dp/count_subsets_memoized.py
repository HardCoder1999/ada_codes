#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
s = int(input())
n = len(ar)

#################################################################
# Memoized Method
#################################################################
t = [[-1 for j in range(s+1)] for i in range(n+1)]

def count_subsets(ar, s, n, t):
    if s == 0:
        return 1
    elif n == 0 and s != 0:
        return 0
    
    if t[n][s] != -1:
        return t[n][s]

    if s >= ar[n-1]:
        t[n][s] = count_subsets(ar, s-ar[n-1], n-1, t) + count_subsets(ar, s, n-1, t)
    elif s < ar[n-1]:
        t[n][s] = count_subsets(ar, s, n-1, t)

    return t[n][s]

print(count_subsets(ar, s, n, t))
