import sys

def solution(gems):
    n = len(gems)
    answer = []
    length = len(list(set(gems)))
    left, right = 0,0
    dic = dict()
    min_value = sys.maxsize
    while right < n:
        if len(dic) < length:
            dic[gems[right]] = right
            right += 1

        if len(dic) == length:
            mini = min(dic.values()) #값중에 가장 작은 인덱스(왼쪽)
            # del dic[gems[left]] #이래버리면  중복 키에 대한 분별을 할 수 없어
            for key, value in dic.items():
                if mini == value:
                    del dic[key]
                    left = value + 1
                    break
                min_value = min(min_value , right-left)

            if min_value > right - left:
                min_value = right - left
                answer = [left,right]
    return answer

