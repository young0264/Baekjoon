import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()
words = []
answer = 0
n , k = map(int,input().split())
for i in range(n):
    words.append(input())
basic_word = ['a','c','n','t','i']
dic = dict()

alphabet = [chr(i) for i in range(97,123)]
for i in alphabet:
    dic[i] = 0
for i in basic_word:
    dic[i] = 1

arr = []
for word in words:
    w = word[4:-4]
    for i in w: #ar,hello,car
        if not dic[i] :
            arr.append(i)

arr = (list(set(arr))) # h,e,l.o,r

new_k = 0
if len(arr) < k-5:
    print(n)
    exit(0)
if k-5 >=0 :
    new_k = k-5
else:
    # new_k = 0
    print(0)
    exit(0)

for i in combinations(arr,new_k):

    new_dic = dict()
    for t in dic:
        new_dic[t] = dic[t]
    for j in i: #combi로 뽑은걸 new_dic에 방문 체크 처리하고
        new_dic[j] = 1

    cnt = 0
    for word in words:  #단어를 하나씩 보았을 때
        flag = 0
        w = word[4:-4] #ar, car, hello ...
        for k in w:
            if not new_dic[k]:#가르치지 않은 단어면은 flag 표시
                flag = True
                break
        if not flag: #flag 표시가 되지 않은 단어면은 cnt += 1
            cnt += 1
    answer = max(answer,cnt)

print(answer)


