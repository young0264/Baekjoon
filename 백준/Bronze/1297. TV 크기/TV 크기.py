D,h,w = map(int,input().split())
answer = 0
k = D/(((h**2)+(w**2))**0.5)
print(int(k*h),int(k*w))

