# 계수 를 생각해서 그 크기로 정렬을 해야함.
# 반례
# 10
# ABB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# 0 ~ 9 사이의 숫자로 알파벳을 변환 가능
import sys
def input():
    return sys.stdin.readline().rstrip()
dic = dict()    #value 값을 기준으로 정렬.
answer = 0
words = []
n = int(input())
number = 9
for i in range(n):
    a = list(input()) #'G' 'C' 'F', ACDEB 각각 input
    words.append(a)
    length = len(a)
    for j in range(length):
        if a[j] not in dic:
            dic[a[j]] = 10**(length-j-1)
        else:
            dic[a[j]] += 10**(length-j-1)
new_dic = dict()
for i in (sorted(dic.items(), key=lambda x : x[1] ,reverse=True)):
    # print("i",i[0],i[1])
    new_dic[i[0]] = number
    number -= 1
for word in words:
    num = ''
    for i in list(word):
        num += str(new_dic[i])
    answer+=int(num)
print(answer)