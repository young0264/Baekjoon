from itertools import combinations
n,l,r,x = map(int,input().split())
arr = list(map(int,input().split()))
visited = [0]*n
box = []
answer = 0
s = set()
dic = dict()
def problem_level(b):
    return l <= sum(b) <= r

def min_max_value(b):
    return x <= (max(b) - min(b))

for i in range(2,n+1):
    for combi in combinations(arr,i):
        # print("combi",combi)
        if problem_level(combi) and min_max_value(combi):
            answer += 1

print(answer)
