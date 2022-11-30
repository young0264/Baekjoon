d,k = map(int,input().split())
fibo = [0]*(31)
fibo[3],fibo[4] = 1,2
for i in range(5,d+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

x,y = fibo[d-1],fibo[d]
if d==3:
    x = 1
A,B = -1,-1
for i in range(1,100001):
    if not (k-x*i) % y :
        A = i
        B = (k-x*i) // y
        break
print(A)
print(B)
