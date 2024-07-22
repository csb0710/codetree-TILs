n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * n for _ in range(4)]

dp[0][1] = arr[1]
dp[1][0] = arr[0]
dp[2][1] = arr[0] + arr[1]

result = 0
for i in range(2, n):
    dp[0][i] = dp[0][i-2] + arr[i]
    dp[1][i] = max(dp[0][i-1], dp[1][i-2]) + arr[i]
    dp[2][i] = max(dp[1][i-1], dp[2][i-2]) + arr[i]
    dp[3][i] = max(dp[2][i-1], dp[3][i-2]) + arr[i]

for i in range(4):
    result = max(result, dp[i][n-1])

print(result)