n = int(input())
arr = list(map(int,input().split()))

a,b = divmod(sum(arr),3)    #3으로 나눈 몫과 나머지

if not b :
    cnt = 0
    for i in arr:
        cnt += i//2
    if cnt >= a:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


