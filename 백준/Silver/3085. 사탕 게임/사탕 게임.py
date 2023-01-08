n = int(input())
graph= [list(input()) for _ in range(n)]
res = 0
dxs,dys = [0,0,1,-1],[1,-1,0,0] #동,서,남,북
answer = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for i in range(n):
    for j in range(n):
        for k in range(4):
            # print("k : ",k)
            dx,dy = i+dxs[k], j+dys[k]
            if in_range(dx,dy) and graph[i][j] != graph[dx][dy]:
                tmp = graph[i][j]
                graph[i][j] = graph[dx][dy]
                graph[dx][dy] = tmp
                arr = graph[i]
                brr = []
                for l in range(n):
                    brr.append(graph[l][j])

                now1 = arr[0]
                count1 = 1
                for t in range(1,n):
                    if arr[t] == now1:
                        count1 += 1
                    else:
                        answer = max(answer,count1)
                        count1 = 1
                        now1 = arr[t]
                # if i==1 and j==2:
                #     print("arr,brr", arr,brr)
                now2 = brr[0]
                count2 = 1
                for t in range(1,n):
                    if brr[t] == now2:
                        count2 += 1
                    else:
                        answer = max(answer,count2)
                        count2 = 1
                        now2 = brr[t]
                answer = max(answer,count1, count2)
                #swap again
                graph[dx][dy] = graph[i][j]
                graph[i][j] = tmp


for i in range(n):
    arr = graph[i][:]
    now = arr[0]
    count = 1
    for j in range(1,n):
        if arr[j] == now:
            count += 1
        else:
            answer = max(answer,count)
            count = 1
            now = arr[j]
    answer = max(answer,count)

for i in range(n):
    arr = []
    for t in range(n):
        arr.append(graph[t][i])
    now = arr[0]
    count = 1
    for j in range(1,n):
        if arr[j] == now:
            count += 1
        else:
            answer = max(answer,count)
            count = 1
            now = arr[j]
    answer = max(answer,count)

print(answer)