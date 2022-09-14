def solution(r, c, board):
    for i in range(r):
        board[i] = list(board[i])
    answer = 0
    def in_range(x,y):
        return 0<=x<r and 0<=y<c
    dx, dy = [0, 1, 0, 1], [0, 0, 1, 1]

    # 현재좌표에서 사각형(우아우아)좌표를 보고 True이면 방문한 visitcnt or false 리턴
    def check(x, y):
        value = board[x][y]
        visitCnt = 0  # 리턴용
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx,ny) and board[nx][ny] == value and not visited[nx][ny] :
                cnt += 1
                visitCnt += 1
            elif in_range(nx,ny) and board[nx][ny] == value:
                cnt += 1

        if cnt == 4:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                visited[nx][ny] = 1
            return visitCnt
        else:
            return False

    def clear():#폭탄 터트리기(아래로 내리기)
        for j in range(c):
            flag = 0
            arr = []
            for i in range(r):
                if visited[i][j]==1:
                    flag = 1
                elif flag == 0 and not visited[i][j]:
                    arr.append(board[i][j])
                elif flag and not visited[i][j]:
                    arr.append(board[i][j])
            # 한 긴 열의 arr 구해졌꼬
            cha = r - len(arr)
            arr = ["0"] * cha + arr  # arr 만들고
            for i in range(r):
                board[i][j] = arr[i]  # board초기화

    while True:
        resFlag = 0
        visited = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] != "0":
                    res = check(i, j)
                    if res :
                        answer += res
                        resFlag = 1

        clear()


        if resFlag == 0:
            break
    return answer

#         if board[x][y] == board[x][y+1] == board[x+1][y] == board[x+1][y+1]:
#             visited[x][y] =1 and visited[x][y+1] =1 and visited[x+1][y] =1 and visited[x+1][y+1] = 1




