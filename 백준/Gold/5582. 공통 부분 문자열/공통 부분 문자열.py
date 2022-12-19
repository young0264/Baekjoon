a = input()
b = input()
answer = 0

dp = [[0]*len(a) for _ in range(len(b))]
lengthA = len(a)
lengthB = len(b)

for i in range(lengthA):
    if a[i]==b[0]:
        dp[0][i] = 1
for i in range(lengthB):
    if a[0] == b[i]:
        dp[i][0] = 1

for i in range(1,lengthB):
    for j in range(1,lengthA):
        if b[i] == a[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])
        # else:
        #     dp[i][j] = max(dp[i])
print(answer)