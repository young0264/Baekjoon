import sys
sys.setrecursionlimit(10**5)
def find(num,dic):
    if num not in dic:
        dic[num] = num+1
        return num
    number = find(dic[num],dic)
    dic[num] = number +1

    return number


def solution(k, room_number):
    answer = []
    dic = dict()
    for num in room_number:
        res = find(num,dic)
        answer.append(res)
    return answer