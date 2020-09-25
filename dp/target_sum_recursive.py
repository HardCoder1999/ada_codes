#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
x = int(input())
n = len(ar)
sum_ = sum(ar)
s = int((sum_ - x)/2)


#################################################################
# Recursive Data
#################################################################
def target_sum(ar, n, s):
    if s == 0:
        return True
    elif n == 0 and s != 0:
        return False

    if s >= ar[n-1]:
        return target_sum(ar, n-1, s-ar[n-1]) + target_sum(ar, n-1, s)
    elif s < ar[n-1]:
        return target_sum(ar, n-1, s)

print(target_sum(ar, n, s))