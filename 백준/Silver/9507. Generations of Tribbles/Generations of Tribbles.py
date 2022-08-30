t = int(input())
dp = [0]*68
def koong(x):
    if x<2 : return 1
    elif x==2 : return 2
    elif x==3 : return 4
    else :
        return koong(x-1) + koong(x-2) + koong(x-3) + koong(x-4)

for i in range(68):
    if i<2 :
        dp[i]= 1
    elif i==2 :
        dp[i]= 2
    elif i==3 :
        dp[i] = 4
    else :
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

for i in range(t):
    n = int(input())
    print(dp[n])