#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
n = len(ar)
sum_ = sum(ar)
x = int(input())
s = int((sum_ - x)/2)

#################################################################
# Memoized Data
#################################################################
t = [[-1 for j in range(s+1)] for i in range(n+1)]

def target_sum(ar, n, s, t):
    if s == 0:
        return 1
    elif n == 0 and s != 0:
        return 0

    if t[n][s] != -1:
        return t[n][s]

    if s >= ar[n-1]:
        t[n][s] = target_sum(ar, n-1, s-ar[n-1], t) + target_sum(ar, n-1, s, t)

    elif s < ar[n-1]:
        t[n][s] = target_sum(ar, n-1, s, t)

    return t[n][s]


print(target_sum(ar, n, s, t))