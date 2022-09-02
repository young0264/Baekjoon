def solution(board, skills):
    r, c = len(board), len(board[0])
    answer = 0
    dp = [[0] * (c + 1) for _ in range(r + 1)]
    for skill in skills:
        s1,s2,e1,e2 = skill[1],skill[2],skill[3],skill[4]
        degree = skill[5]

        #공격이라 체력이 깎이는 부분
        if skill[0] == 1:
            dp[s1][s2] += -degree
            dp[e1+1][e2+1] += -degree
            dp[s1][e2+1] += degree
            dp[e1+1][s2] += degree

        #힐링이라 체력이 차오르는 부분
        elif skill[0] == 2:
            dp[s1][s2] += degree
            dp[e1 + 1][e2 + 1] += degree
            dp[s1][e2 + 1] += -degree
            dp[e1 + 1][s2] += -degree


    #행아래로 누적합
    for i in range(1,r+1):
        for j in range(c+1):
            dp[i][j] = dp[i-1][j] + dp[i][j]
    #열오른쪽으로 누적합
    for j in range(1,c+1):
        for i in range(r+1):
            dp[i][j] = dp[i][j] + dp[i][j-1]
   
    for i in range(r):
        for j in range(c):
            res = board[i][j] + dp[i][j]
            if res >0:
                answer += 1

    return answer

