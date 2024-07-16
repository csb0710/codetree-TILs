n = int(input())

arr = [[0]*n for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

result = [[0]*n for _ in range(n)]

result[0][0] = 1
arr[n-1][n-1] = 1

for i in range(n):
    for j in range(i, n):
        tempx = i + arr[i][j]
        tempy = j + arr[i][j]
        if tempx < n:
            result[tempx][j] += result[i][j]
        if tempy < n:
            result[i][tempy] += result[i][j]
    for j in range(i+1, n):
        tempx = j + arr[j][i]
        tempy = i + arr[j][i]
        if tempx < n:
            result[tempx][i] += result[j][i]
        if tempy < n:
            result[j][tempy] += result[j][i]
  
print(result[n-1][n-1])