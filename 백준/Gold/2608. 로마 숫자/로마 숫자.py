# IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900
#	I	V	X	L	C	D	M
#	1	5	10	50	100	500	1000
import sys
def input():
    return sys.stdin.readline().rstrip()
a = list(input())
visited_a = [0] * len(a)
a2 = ''
b = list(input())
visited_b = [0] * len(b)
b2 = ''
# VLD 1번 4개는3번
dic1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
dic2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

# idx매칭 , arr의 숫자에 맞는 갯수 배열brr
dic_arr = ['I', 'IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
arr = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
brr = [3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3]
sum_value = 0

for i in range(len(a) - 1):
    if not visited_a[i]:
        if dic1[a[i]] < dic1[a[i + 1]]:
            visited_a[i], visited_a[i + 1] = 1, 1
            res = a[i] + a[i + 1]
            sum_value += dic2[res]
        else:
            sum_value += dic1[a[i]]
            visited_a[i] = 1

for i in range(len(b) - 1):
    if not visited_b[i]:
        if dic1[b[i]] < dic1[b[i + 1]]:
            visited_b[i], visited_b[i + 1] = 1, 1
            res = b[i] + b[i + 1]
            sum_value += dic2[res]
        else:
            visited_b[i] = 1
            sum_value += dic1[b[i]]
# print(visited_a)
# print(visited_b)
if not visited_a[-1]:
    sum_value += dic1[a[-1]]
    visited_a[-1]=1
if not visited_b[-1]:
    sum_value += dic1[b[-1]]
    visited_b[-1]=1

# if dic1[a[-2]] >= dic1[a[-1]]:
#     sum_value += dic1[a[-1]]
# if dic1[b[-2]] >= dic1[b[-1]]:
#     sum_value += dic1[b[-1]]
answer = ''
# brr 이 0보다 크고 현재값이 arr idx보다 크면.
# print(arr[-13])
print(sum_value)
for i in range(-1, -14, -1):
    while sum_value >= arr[i] :
        if brr[i] > 0:
            brr[i] -= 1
            sum_value -= arr[i]
            answer += dic_arr[i]

print(answer)
