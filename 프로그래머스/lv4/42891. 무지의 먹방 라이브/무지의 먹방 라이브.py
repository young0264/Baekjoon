def solution(food_times, k):
    answer = 0
    idx = 0
    length = len(food_times)

    while k:
        if food_times[idx % length]:
            food_times[idx % length] -= 1
            idx += 1
            k -= 1
        else:
            idx += 1
            continue
    answer = food_times[idx % length+1]
    return answer+1

food_times = [3, 1, 2]
k = 5
(solution(food_times, k))
