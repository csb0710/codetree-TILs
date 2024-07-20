n = int(input())
user_input = input().strip()
    
arr = list(map(int, user_input.split()))

result = -1001
temp = 0
for i in range(n):
    temp += arr[i]
    result = max(result, temp)
    if temp < 0 :
        temp = 0
    

print(result)