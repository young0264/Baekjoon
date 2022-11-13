r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]
answer = []
dic = dict()
dic[46] = 46
dic[79] = 79
dic[45] = 124
dic[124] = 45
dic[47] = 92
dic[92] = 47
dic[94] = 60
dic[60] = 118
dic[118] = 62
dic[62] = 94

def change(num):
    res = dic[num]
    return chr(res)


for j in range(c-1,-1,-1):
    arr = ''
    for i in range(r):
        res = change(ord(graph[i][j]))
        arr += res
    answer.append(arr)
    print(arr)
# for i in answer:
#     print(*i)


