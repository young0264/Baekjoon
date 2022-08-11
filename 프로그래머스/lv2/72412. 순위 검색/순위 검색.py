from bisect import bisect_left
from collections import defaultdict
from itertools import combinations
def solution(info, query):
    answer = []
    dic = defaultdict(list)

    for inf in info:
        inf = inf.split(' ')
        info_key = inf[0:-1]
        info_value = int(inf[-1])
        for i in range(5):
            combi = list(combinations(info_key,i))
            for j in combi:
                res = ''.join(j)
                dic[res].append(info_value)
    for key in dic:
        dic[key].sort()
    for q in query:
        q = q.split(' ')
        q_key = q[:-1]
        q_value = int(q[-1])

        for i in range(3):
            q_key.remove('and')

        while '-' in q_key:
            q_key.remove('-')
        query_key = ''.join(q_key)


        if query_key in dic:
            scoreList = dic[query_key]

            if len(scoreList) > 0:
                left, right = 0, len(scoreList)
                while left < right:
                    mid = (left + right) // 2
                    if scoreList[mid] >= q_value:
                        right = mid
                    else:
                        left = mid + 1
                answer.append(len(scoreList) - left)
        else:
            answer.append(0)

    return answer