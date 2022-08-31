prohibit = input()
dic = dict()
for i in 'CAMBRIDGE':
    dic[i] = 1
answer = ''
for i in prohibit:
    if i not in dic:
        answer += i
print(answer)
