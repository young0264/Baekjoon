r, c = map(int,input().split())
graph = []
answer = 0
for _ in range(r):
    graph.append(list(input()))

def reverse(x,y):
    for i in range(x+1):
        for j in range(y+1):
            if graph[i][j]=="1":
                graph[i][j] = "0"
            else:
                graph[i][j] = "1"
def check(x,y):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "1":
                return False
    return True

for i in range(r-1,-1,-1):
    for j in range(c-1,-1,-1):
        if graph[i][j] == "1":
            reverse(i,j)
            answer += 1
        if check(i,j):
            print(answer)
            exit(0)
