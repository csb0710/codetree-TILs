n = int(input())

arr = [[0]*n for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

result = [[0]*n for _ in range(n)]
q = []
q.append([0, 0, 1])

x = [1, 0]
y = [0, 1]

while len(q) != 0:
    temp = q.pop(0)
    tempx = temp[0]
    tempy = temp[1]
    result[tempx][tempy] += temp[2]

    if tempx == n-1 and tempy == n-1:
        continue

    for i in range(2):
        tempxx = tempx + x[i] * arr[tempx][tempy]
        tempyy = tempy + y[i] * arr[tempx][tempy]

        if tempxx < 0 or tempxx >= n or tempyy < 0 or tempyy >= n:
            continue

        q.append([tempxx, tempyy, result[tempx][tempy]])

print(result[n-1][n-1])