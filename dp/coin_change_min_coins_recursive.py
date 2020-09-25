#################################################################
# Input Data
#################################################################
coins = list(map(int, input().split()))
amount = int(input())
n = len(coins)

#################################################################
# Recursive Method
#################################################################
def coin_change(coins, amount, n):
    if n == 0:
        return 10**9
    elif amount == 0 and n != 0:
        return 0

    if amount >= coins[n-1]:
        return min(1+coin_change(coins, amount-coins[n-1], n), coin_change(coins, amount, n-1))
    elif amount < coins[n-1]:
        return coin_change(coins, amount, n-1)

print(coin_change(coins, amount, n))