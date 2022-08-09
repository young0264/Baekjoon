

def solution(n, t, m, p):

    answer = ''
    arr = ['0'] * (t * m+1)
    length = t*m
    dic = {10:'A', 11:'B', 12:'C',13:'D',14:'E',15:'F'}
    def find(n, k):  # 숫자 n의 k진수구하기
        res = ''
        while n:
            n, mod = divmod(n, k)
            if mod in dic:
                res += dic[mod]
            else:
                res += str(mod)
        return res[::-1]
    idx,num,flag = 1,1,0

    while True:
        result = find(num, n)
        for i in result:
            arr[idx] = i
            idx += 1
            if idx == length + 1:
                flag = 1
                break
        if flag:
            break
        num += 1

    for i in range(t):
        answer += arr[p+m*i-1]

    return answer






