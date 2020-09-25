l = list(map(int, input().split()))
n = len(l)
# Sort the volume of petrols.
l.sort()
x = l[n-1]
y = 0

for i in range(n-2, -1, -1):
    if x <= y:
        x += l[i]
    else:
        y += l[i]

print(x, y)
    