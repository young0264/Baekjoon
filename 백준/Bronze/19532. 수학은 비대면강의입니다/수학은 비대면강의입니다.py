a,b,c,d,e,f = list(map(int,input().split()))
x,y = 0,0
# dar, dbr = arr[:3], arr[3:]
# ar = arr[:3]
# br = arr[3:]
# a_value, b_value = ar[0],br[0]
#
# # for i in range(3):
# #     br[i] = br[i]*a_value
# #     ar[i] = ar[i]*b_value
#
# if ar[1] != br[1]:
#     y = (ar[2]-br[2])//(ar[1]-br[1])
# else:
#     print(1, 1)
#     exit(0)
# if ar[0] != 0:
#     x = (ar[2]-ar[1]*y)//ar[0]
# else:
#     x = (dbr[2]-dbr[1]*y)
#
# print(x,y)
for i in range(-999,1000):
    for j in range(-999,1000):
        if a*i+b*j ==c and d*i+e*j==f:
            print(i,j)
            exit(0)