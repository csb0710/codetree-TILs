n = int(input())
arr = list(map(int, input().split(' ')))

result = -1001
temp = 0
for i in range(n):
    temp += arr[i]
    result = max(result, temp)
    if temp < 0 :
        temp = 0
    

print(result)