import math
def solution(n, k):
    answer = 0

    def change(n,k):
        res = ''
        while n>0:
            n,mod = divmod(n,k)
            res+=str(mod)
        return res[::-1]

    def prime_number(x):
        for i in range(2,int(math.sqrt(x))+1):
            if x%i ==0:
                return False
        return True


    currentNum = change(n,k)
    res =  currentNum.split('0')
    for i in res:
        if i =='':
            continue
        elif int(i) == 1:
            continue
        elif prime_number(int(i)):
            print("i",i)
            answer += 1
    return answer

