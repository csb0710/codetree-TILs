n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key = lambda x:x[1])

result = 0
check = 0

for i in range(n):
    if arr[i][0] >= check:
        result += 1
        check = arr[i][1]

print(result)