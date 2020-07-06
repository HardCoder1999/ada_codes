#################################################################
# Input Data
#################################################################
a = input()
b = input()
n = len(a)
m = len(b)

#################################################################
# Recursive Method
#################################################################
def lcs(a, b, n, m, max_val):
    if n == 0 or m == 0:
        return 0
    
    if a[n-1] == b[m-1]:
        return lcs(a, b, n-1, m-1, max_val+1)

    else:
        return max(max_val, lcs(a, b, n-1, m, max_val), lcs(a, b, n, m-1, max_val))

print(lcs(a, b, n, m, 0))