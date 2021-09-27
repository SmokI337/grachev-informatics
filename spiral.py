i = int(input())
n = 2 * i + 1
a = [[0 for j in range(n)] for i in range(n)]

L = i  # left
R = i  # right
T = i  # top
B = i  # bottom
k = 0
x = i
y = i

while k < n ** 2:
    while x > L:
        a[x][y] = k
        k += 1
        x -= 1
    while y < B:
        a[x][y] = k
        k += 1
        y += 1
    while x < R:
        a[x][y] = k
        k += 1
        x += 1
    while y > T:
        a[x][y] = k
        k += 1
        y -= 1
    L -= 1
    R += 1
    T -= 1
    B += 1

for i in range(n):
    print(*a[i])
