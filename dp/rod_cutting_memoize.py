#################################################################
# Input Data
#################################################################
length = list(map(int, input().split()))
price = list(map(int, input().split()))
l = int(input())
n = len(length)

#################################################################
# Memoization Method
#################################################################
t = [[-1 for j in range(l+1)] for i in range(n+1)]
def rod_cutting(length, price, n, l, t):
    if n == 0 or l == 0:
        return 0

    if t[n][l] != -1:
        return t[n][l]

    if l >= length[n-1]:
        t[n][l] = max(price[n-1] + rod_cutting(length, price, n, l-length[n-1], t), rod_cutting(length, price, n-1, l, t))
    
    elif l < length[n-1]:
        t[n][l] = rod_cutting(length, price, n-1, l, t)

    return t[n][l]

print(rod_cutting(length, price, n, l, t)) 
