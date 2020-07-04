#################################################################
# Input Data
#################################################################
length = list(map(int, input().split()))
price = list(map(int, input().split()))
l = int(input())
n = len(length)

#################################################################
# Recursive Method
#################################################################
def rod_cutting(length, price, n, l):
    if l == 0 or n == 0:
        return 0
    
    if l >= length[n-1]:
        return max(price[n-1] + rod_cutting(length, price, n, l-length[n-1]), rod_cutting(length, price, n-1, l))
        
    elif  l < length[n-1]:
        return rod_cutting(length, price, n, l)

print(rod_cutting(length, price, n, l))