#################################################################
# Input Data
#################################################################
coins = list(map(int, input().split()))
amount = int(input())
n = len(coins)

#################################################################
# Dynamic Programming Method
#################################################################
t = [[0 for j in range(amount+1)] for i in range(n+1)]
for j in range(amount+1):
    t[0][j] = 10**9 


for i in range(1, n+1):
    for j in range(1, amount+1):
        if j >= coins[i-1]:
            t[i][j] = min(1+t[i][j-coins[i-1]], t[i-1][j])
        elif j < coins[i-1]:
            t[i][j] = t[i-1][j]

print(t[n][amount])