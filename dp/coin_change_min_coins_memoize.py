#################################################################
# Input Data
#################################################################
coins = list(map(int, input().split()))
amount = int(input())
n = len(coins)

#################################################################
# Memoization Method
#################################################################
t = [[-1 for j in range(amount+1)] for i in range(n+1)]

def coin_change(coins, amount, n):
    if n == 0:
        return 10**9
    elif amount == 0:
        return 0
    if t[n][amount] != -1:
        return t[n][amount]

    if amount >= coins[n-1]:
        t[n][amount] = min(1+coin_change(coins, amount-coins[n-1], n), coin_change(coins, amount, n-1))

    elif amount < coins[n-1]:
        t[n][amount] = coin_change(coins, amount, n-1)

    return t[n][amount]

print(coin_change(coins, amount, n))
