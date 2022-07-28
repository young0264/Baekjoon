from itertools import permutations


def solution(expression):

    def init():
        for i in range(len(basic_expressions)):
            new_expressions[i] = basic_expressions[i]

    basic_expressions = []
    new_expressions = []
    num = ''


    for i in list(expression):
        if 48 <= ord(i) <= 57:
            num += i
        else:
            basic_expressions.append(int(num))
            num = ''
            basic_expressions.append(i)
    basic_expressions.append(num)

    answer = 0
    operators = ['*', '+', '-']
    for i in permutations(operators, 3):
        new_expressions[:] = basic_expressions[:]
        for operator in i:
            while operator in new_expressions:
                idx = new_expressions.index(operator)
                num = 0
                if new_expressions[idx] == '*':
                    num = int(new_expressions[idx - 1]) * int(new_expressions[idx + 1])
                elif new_expressions[idx] == "+":
                    num = int(new_expressions[idx - 1]) + int(new_expressions[idx + 1])
                elif new_expressions[idx] == '-':
                    num = int(new_expressions[idx - 1]) - int(new_expressions[idx + 1])
                new_expressions = new_expressions[:idx-1] + [num] + new_expressions[idx + 2:]
        answer = max(answer,abs(num))
    return answer


