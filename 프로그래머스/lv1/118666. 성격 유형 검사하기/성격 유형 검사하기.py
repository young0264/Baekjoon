def solution(survey, choices):
    answer = ''
    choice_board = {1:3,2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    dic = dict()
    n = len(choices)
    res = ''
    sung = [['R','T'],['C','F'],['J','M'],['A','N']]
    for i in range(4):
        a,b = sung[i]
        if a not in dic:
            dic[a] = 0
        if b not in dic:
            dic[b] = 0
    for i in range(n):
        if choices[i] < 4:
            dic[survey[i][0]] += choice_board[choices[i]]
        elif choices[i] > 4:
            dic[survey[i][1]] += choice_board[choices[i]]
    # print(dic)

    #지표
    for i in range(4):
        a,b = sung[i]
        if dic[a] >= dic[b]:
            answer += a
        elif dic[b] > dic[a]:
            answer += b

    # print(sung)
    # print(dic)
    # print(answer)

    return answer
survey = ["AN", "CF", "MJ", "RT", "NA"]
# survey = ["TR", "RT", "TR"]
choices = [5, 3, 2, 7, 5]
# choices = [7, 1, 3]
solution(survey, choices)
