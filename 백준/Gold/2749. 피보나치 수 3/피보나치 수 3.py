n = int(input())
M= 1000000
P = 1500000 #주기
n=n%P
a,b = 0,1
for i in range(n):
    a,b = b%M, (a+b)%M
print(a)