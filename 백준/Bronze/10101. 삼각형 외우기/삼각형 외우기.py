

# value = 0
# flag = 1
# a = int(input())
# b = int(input())
# c = int(input())
# value = a+b+c
# arr = [a,b,c]
# if value == 180:
#     if a==b==c==60:
#         print('Equilateral')
#     elif len(set(arr))==2:
#         print('Isosceles')
#     elif len(set(arr))==3:
#         print('Scalene')
# else:
#     print('Error')


arr = []
value = 0
for i in range(3):
    n = int(input())
    arr.append(n)
    value += n

length = len(set(arr))
if value == 180:

    if length == 1:
        print("Equilateral")
    elif length == 2:
        print('Isosceles')
    elif length == 3:
        print('Scalene')
else:
    print('Error')