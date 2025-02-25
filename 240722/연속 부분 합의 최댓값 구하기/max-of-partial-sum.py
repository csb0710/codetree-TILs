n = int(input())
arr = list(map(int, input().split()))
dp = [-2001] * n
dp[0] = arr[0]

result = dp[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
    result = max(result, dp[i])

print(result)