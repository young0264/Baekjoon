import math, sys
input= sys.stdin.readline
arr = [True for i in range(1000001)]
primelist = []
def prime_list(x):
    global primelist
    for i in range(2,int(math.sqrt(1000000))+1):
        if arr[i] == True:
            for j in range(i+i,1000001,i):
                arr[j] = False
    primelist = [i for i in range(2,1000001) if arr[i]==True]
prime_list(1000000)
#print(primelist)    #소수 리스트를 구하고
while True:
    n = int(input())
    if not n:
        break       #2개의 소수로 값을 만드는 것이기 때문에 primelist에서 숫자를 작은거부터 빼면서
                        #그 수에 대응되는 숫자는 하나뿐. 그러니 그 대응되는 숫자가 소수인지만(True)
                        #확인후 출력
    for i in primelist:
        if arr[n-i] :
            print('%d = %d + %d' %(n,i,n-i))
            break
