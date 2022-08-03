from itertools import combinations
def solution(orders, course):
    answer = []
    dic = dict()
    for i in orders:
        length = len(list(i))
        for j in range(2,length+1):
            for t in combinations(list(i),j):
                t=sorted(t)
                x= ''.join(t)
                
                if x not in dic:
                    dic[x] = 1
                else:
                    dic[x] += 1
        
    if 'AB' in dic:
        print(dic['AB'])
    for j in course:
        max_value = 1
        res = []
        
        for i in dic:
            if len(list(i)) == j:
                if dic[i] > max_value:
                    max_value = dic[i]
                    res = [i]
                elif dic[i]>1 and dic[i] == max_value:
                    res.append(i)
                    
        for i in res:
            answer.append(i)
                    
                
        
    answer.sort()
    return answer