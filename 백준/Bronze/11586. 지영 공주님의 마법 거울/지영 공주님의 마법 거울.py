t= int(input())
graph = []
for i in range(t):
    s = input()
    graph.append(s)
n= int(input())

if n == 1:
    for i in graph:
        print(i)
elif n==2:
    for i in range(t):
        res= ''
        for j in range(t-1,-1,-1):
            res+=graph[i][j]
        print(res)

else:

    for i in range(t-1,-1,-1):
        res = ''
        for j in range(t):
            res +=graph[i][j]
        print(res)
