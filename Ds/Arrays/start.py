import numpy as np

l_min = int(input())
l_max = int(input())
b_min = int(input())
b_max = int(input())

#t = [[-1 for i in range(b_max+1)] for j in range(l_max+1)]
#t = [[0]*(b_max+1)]*(l_max+1)
t = np.zeros((l_max+1, b_max+1))
count = 0

for i in range(1, l_max+1):
  t[i][1] = i

for j in range(1, b_max+1):
  t[1][j] = j

for i in range(2, l_max+1):
  for j in range(2, b_max+1):
    if i == j:
      t[i][j] = 1
    elif i < j:
      t[i][j] = t[i][i] + t[i][j-i]
    else:
      t[i][j] = t[i-j][j] + t[j][j]

    if i >= l_min and j >= b_min:
      count += t[i][j]

print(count)
