import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    heap = []
    length = len(food_times)
    # 0번째 : 음식 숫자, 1번째: 음식숫자에 해당하는 food_times의 인덱스
    for i in range(length):
        heapq.heappush(heap,(food_times[i],i+1))
    count = 0
    while heap:
        # print("heap = ", heap)
        # print(k,heap)
        if k - (heap[0][0]-count)*length >= 0:
            k -= (heap[0][0]-count)*length
            count = heap[0][0]
            heapq.heappop(heap)
            length -= 1
        else:
            # print(123)
            heap.sort(key=lambda x : x[1])
            answer = heap[k%length][1]
            # print("ans",answer)
            # print(res[1],123)
            # print(answer)
            break
#줄어드는 길이

    return answer

food_times , k= [3, 1, 2] , 5
solution(food_times, k)