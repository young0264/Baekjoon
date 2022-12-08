dp = [[[0]*101 for _ in range(101)] for _ in range(101)]

dp[70][70][70] = 1048576
#0~100까지
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i<=50 or j<=50 or k<=50:
                dp[i][j][k] = 1
            elif i>70 or j>70 or k>70:
                dp[i][j][k] = dp[70][70][70]
                # if i==69 and j==70 and k==71:
                #     print(123123)
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1]-dp[i-1][j-1][k-1]

# print(dp[70][70][70])

while True:
    a,b,c = map(int,input().split())
    res = (dp[a+50][b+50][c+50])
    if a==-1 and b==-1 and c==-1:
        break
    print("w(%d, %d, %d) = %d" %(a,b,c,res))
# for i in dp:
#     print(i)
# def f(a,b,c):

