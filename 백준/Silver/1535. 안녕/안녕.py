n = int(input())
HP = [0] + list(map(int, input().split()))  # 잃는 체력
Happy = [0] + list(map(int, input().split()))  # 얻는 기쁨

dp = [[0] * (101) for _ in range(n + 1)]
answer = 0
for i in range(1, n + 1):
    for j in range(1, 101):
        if (100 - j) - HP[i] >= 0:
            dp[i][100 - j] = max(dp[i - 1][100 - j - HP[i]] + Happy[i], dp[i - 1][100 - j])
        else:
            dp[i][100 - j] = dp[i - 1][100 - j]
        answer = max(answer, dp[i][100 - j])


# print(dp[-1][-2])
print(answer)
