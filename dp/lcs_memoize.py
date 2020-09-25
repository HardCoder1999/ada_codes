#################################################################
# Input Data
#################################################################
a = input()
b = input()
n = len(a)
m = len(b)

#################################################################
# Memoization Method
#################################################################
t = [[-1 for j in range(m+1)] for i in range(n+1)]

def lcs(a, b, n, m, t):
    if n == 0 or m == 0:
        return 0
    
    if t[n][m] != -1:
        return t[n][m]
    
    if a[n-1] == b[m-1]:
        t[n][m] = 1 + lcs(a, b, n-1, m-1, t)

    else:
        t[n][m] = max(lcs(a, b, n-1, m, t), lcs(a, b, n, m-1, t))

    return t[n][m]

print(lcs(a, b, n, m, t))