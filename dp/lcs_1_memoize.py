#################################################################
# Input Data
#################################################################
a = input()
b = input()
n = len(a)
m = len(b)

#################################################################
# Memoization Method
#################################################################
# t = [[-1 for j in range(m+1)] for i in range(n+1)]


# def lcs(a, b, n, m, t, max_val):
#     if n == 0 or m == 0:
#         return 0

#     if t[n][m] != -1:
#         return t[n][m]

#     if a[n-1] == b[m-1]:
#         t[n][m] = lcs(a, b, n-1, m-1, t, max_val+1)
#         max_val = max(max_val, t[n][m])
#     else:
#         t[n][m] = max(max_val, lcs(a, b, n-1, m, t, 0),
#                       lcs(a, b, n, m-1, t, 0))

#     return t[n][m]


# print(lcs(a, b, n, m, t, 0))
