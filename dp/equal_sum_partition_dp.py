#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
ar_sum = sum(ar)
n = len(ar)

#################################################################
# Dynamic Programming method
#################################################################
if ar_sum % 2 != 0:
    print(False)
else:
    s = ar_sum // 2
    t = [[False for j in range(s+1)] for i in range(n+1)]
    for i in range(n+1):
        t[i][0] = True

    for i in range(n+1):
        for j in range(s+1):
            if j >= ar[i-1]:
                t[i][j] = t[i-1][j-ar[i-1]] or t[i-1][j]
            elif j < ar[i-1]:
                t[i][j] = t[i-1][j]
    print(t[n][s])
