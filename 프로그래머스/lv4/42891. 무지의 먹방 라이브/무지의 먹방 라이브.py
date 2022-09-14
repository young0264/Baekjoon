import heapq

def solution(food_times, k):
    if sum(food_times) <=k:
        return -1
    answer = 0
    length = len(food_times)
    pre_length = 0
    heap = []

    for i in range(length):
        heapq.heappush(heap,(food_times[i],i+1))
    # print("heap",heap)
    while heap:
        res = length*(heap[0][0]-pre_length)
        if res <= k:    #진행
            pre_length = heap[0][0]
            heapq.heappop(heap)
            length -= 1
            k -= res
        else:
            idx = k%length
            heap.sort(key=lambda x : x[1])
            answer = heap[idx][1]
            # print(res)
            # print(heap)
            break
    # print(answer)
    return answer


food_times, k = [3, 1, 2], 5
solution(food_times, k)

