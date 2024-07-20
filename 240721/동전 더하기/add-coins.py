n, k = map(int, input().split())

arr = [0] * n

for i in range(n-1, -1, -1):
    arr[i] = int(input())

result = 0
index = 0

while k > 0 and index < n:
    result += k // arr[index]
    k = k % arr[index]
    index += 1

print(result)