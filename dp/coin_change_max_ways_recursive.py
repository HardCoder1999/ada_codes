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
    if amount == 0:
        return 1
    elif n == 0 and amount != 0:
        return 0
        
    if amount >= coins[n-1]:
        return coin_change(coins, amount-coins[n-1], n) + coin_change(coins, amount, n-1)
    elif amount < coins[n-1]:
        return coin_change(coins, amount, n-1)

print(coin_change(coins, amount, n))