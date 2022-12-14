a = input()
b = input()
length_a = len(a)
length_b = len(b)
dp = [[0]*(length_b+1) for _ in range(length_a+1)]
answer = 0

for i in range(length_a):
    if b[0] == a[i]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i-1][0]

for i in range(length_b):
    if a[0] == b[i]:
        dp[0][i] = 1
    else:
        dp[0][i] = dp[0][i-1]

for i in range(1, length_a):
    for j in range(1, length_b):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        answer = max(answer, dp[i][j])

print(answer)
# for i in dp:
#     print(*i)