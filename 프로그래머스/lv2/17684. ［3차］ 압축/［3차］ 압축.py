def solution(msg):
    answer = []

    dic = dict()
    alpha = ''
    for i in range(26):
        dic[chr(65 + i)] = i + 1
    idx = 26
    for i in list(msg):
        alpha += i
        if alpha not in dic:
            idx += 1
            dic[alpha] = idx
            answer.append(dic[alpha[:-1]])
            alpha = alpha[-1]
    answer.append(dic[alpha])
    return answer
