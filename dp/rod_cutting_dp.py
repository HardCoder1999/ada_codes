#################################################################
# Input Data
#################################################################
length = list(map(int, input().split()))
price = list(map(int, input().split()))
l = int(input())
n = len(length)

#################################################################
# Dynamic Programming Method
#################################################################
t = [[0 for j in range(l+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, l+1):
        if j >= length[i-1]:
            t[i][j] = max(price[i-1]+t[i][j-length[i-1]], t[i-1][j])

        elif j < length[i-1]:
            t[i][j] = t[i-1][j]

print(t[n][l]) 