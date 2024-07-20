n = int(input())
arr = list(map(int, input().split(' ')))

result = 0
temp = 0
for i in range(n):
    temp += arr[i]
    if temp < 0 :
        temp = 0
    result = max(result, temp)

print(result)