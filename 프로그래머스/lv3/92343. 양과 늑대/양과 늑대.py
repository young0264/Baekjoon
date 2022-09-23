def solution(info, edges):
    global answer

    def dfs(dx, sheep, wolf,box):
        global answer
        if info[dx] == 0:   #양일때
            sheep += 1
            answer = max(answer,sheep)
        else:               #늑대일때
            wolf += 1
        if wolf >= sheep :
            return
        
        box.extend(edges_arr[dx])   #dx의 자식들을 box에 추가해줌
        
        for nx in box:
            # arr = []
            # for nnx in box:
            #     if nnx != nx:
            #         arr.append(nnx)
            new_box = box[::]
            new_box.remove(nx)
            dfs(nx,sheep,wolf,new_box)
            # dfs(nx,sheep, wolf, arr)

    answer = 0
    # visited = [0] * len(info)
    edges_arr = [[] for _ in range(len(info))] #binary tree 정보

    for i in range(len(edges)):
        parent, child = edges[i][0], edges[i][1]
        edges_arr[parent].append(child)
    print(edges_arr)
    dfs(0, 0, 0,[])
    return answer
