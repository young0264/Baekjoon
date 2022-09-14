n, d, k, c = map(int,input().split())
arr = []
dic = dict()
max_length = 0
answer = []
for i in range(n):
    arr.append(int(input()))

arr = arr*2
for i in (arr[:k]):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
# print("12321312",dic)
max_length = len(dic)

for i in range(2*n-k):
    # print("dic",dic,max_length)
    # print("i",i)
    #왼쪽포인트가 딕셔너리에 값이 있는데 1이면 delete, else: -1
    if arr[i] in dic :
        if dic[arr[i]] == 1:
            del dic[arr[i]]
        else:
            dic[arr[i]] -= 1

    #오른쪽포인트가 딕셔너리에 있으면 +1 아니면 생성
    if arr[i+k] in dic:
        dic[arr[i+k]] += 1
    else:
        dic[arr[i+k]] = 1

    #딕셔너리 길이가 최대길이보다 더 크면 길이값 초기화
    if len(dic)>max_length:
        max_length = len(dic)
        answer = []
        for d in dic:
            answer.append(d)
    elif len(dic) == max_length:
        if not answer :
            for d in dic:
                answer.append(d)
        else:
            if c not in dic:
                answer = []
                for d in dic:
                    answer.append(d)
    max_length = max(max_length,len(dic))

    # print()
# print("max_length",max_length)
if c in answer:
    print(len(answer))
else:
    print(len(answer)+1)
# print(answer)