n, k = map(int, input().split())

arr = []
result = [0] * (k+1)

for _ in range(n):
    w, v = map(int, input().split())
    arr.append([w, v])

arr.sort(key=lambda x: x[0])

for i in range(n):
    tempw = arr[i][0]
    tempv = arr[i][1]

    for j in range(k - tempw, -1, -1):
        result[j + tempw] = max(result[j] + tempv, result[j + tempw])

output = 0

for i in range(k+1):
    output = max(output, result[i])

print(output)