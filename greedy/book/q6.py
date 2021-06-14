import heapq


# 우선순위 큐를 생각하자
# food_times 는 각 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열이다.
# k 는 방송이 중단된 시간을 나타낸다.
# 만약 더 섭취해야 할 음식이 없다면 -1을 반환하면 된다.
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    # 먹기 위해 사용한 시간
    sum_value = 0
    # 직전에 다 먹은 음식 시간
    previous = 0
    # 남은 음식의 갯수
    length = len(food_times)
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]
