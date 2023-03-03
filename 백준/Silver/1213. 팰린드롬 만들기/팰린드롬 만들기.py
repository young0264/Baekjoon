s = list(input())
length = len(s)
dic = dict()

s.sort()

for i in s:
    dic[i] = dic.get(i,0)+1
odd_num = 0
center = ""

for i in dic:
    if dic[i]%2 :
        odd_num += 1
        center = i
        if dic[i] == 1:
            dic[i] = 0

if length%2 and odd_num > 1:
    print("I'm Sorry Hansoo")
    exit(0)
elif length%2 == 0 and odd_num > 0:
    print("I'm Sorry Hansoo")
    exit(0)

answer = ""
for i in dic:
    num = dic[i]//2
    answer += i*num
res = ""
if center:
    answer = (answer + center + answer[::-1])
else:
    answer = (answer + answer[::-1])
print(answer)