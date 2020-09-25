#################################################################
# Input Data
#################################################################
ar = list(map(int, input().split()))
s = int(input())
n = len(ar)

#################################################################
# Recursive method
#################################################################
def count_subset(ar, s, n):
    if s == 0:
        return True
    elif n == 0 and s != 0:
        return False
    else:
        if s >= ar[n-1]:
            return count_subset(ar, s-ar[n-1], n-1) + count_subset(ar, s, n-1)
        elif s < ar[n-1]:
            return count_subset(ar, s, n-1)

print(count_subset(ar, s, n))
