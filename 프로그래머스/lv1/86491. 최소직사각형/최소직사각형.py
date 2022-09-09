import sys

def solution(sizes):
    answer = 0
    min_value = 0
    max_value = 0
    for a,b in sizes:
        min_size = min(a,b)
        max_size = max(a,b)
        min_value = max(min_value,min_size)
        max_value = max(max_value,max_size)
    answer = (min_value* max_value)

    return answer


