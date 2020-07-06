#################################################################
# Input Data
#################################################################
a = input()
b = input()
n = len(a)
m = len(b)
result = 0
#################################################################
# Dynamic Programming Method
#################################################################
t = [[0 for j in range(m+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            t[i][j] = 1 + t[i-1][j-1]
            result = max(result, t[i][j])
        else:
            t[i][j] = 0

print(result)
