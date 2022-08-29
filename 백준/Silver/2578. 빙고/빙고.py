bingo = [list(map(int,input().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]

def check(x):
    cnt = 0
    d1,d2 = 1,1

    #가로줄 체크
    for i in range(5):
        flag = 0
        for j in range(5):
            if not visited[i][j]:
                flag = 1
        if not flag :
            cnt += 1

    #세로줄체크
    for j in range(5):
        flag = 0
        for i in range(5):
            if not visited[i][j]:
                flag = 1
        if not flag:
            cnt += 1

    tflag1, tflag2 = 0,0

    for i in range(5):
        if not visited[i][i]:
            tflag1 = 1
            break
    if not tflag1:
        cnt += 1

    for i in range(5):
        if not visited[i][4-i]:
            tflag2 = 1
            break
    if not tflag2:
        cnt += 1

    #valid
    if cnt>=3:
        return True
    return False

def double(x):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == x:
                visited[i][j] = 1

answer = 0
for i in range(5):
    arr = list(map(int,input().split()))
    for j in arr:
        answer += 1
        double(j)
        if check(j) :
            # print("12321",i,j,answer)
            print(answer)
            exit(0)
            # for t in visited:
            #     print(*t)
            # print()

