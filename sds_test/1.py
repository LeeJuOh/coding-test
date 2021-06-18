import sys
import heapq
from collections import deque


def find_shortest_time(N: int, times: deque) -> int:
    result = 0
    if len(times) == 1:
        result = times[0]
    else:
        priority_q = []
        direction = 1
        first_time = 0
        second_time = 0
        min_time = 0
        while True:
            times = deque(sorted(times))
            if direction == 1:
                first_time = times.popleft()
                second_time = times.popleft()
            else:
                second_time = times.pop()
                first_time = times.pop()
            result += second_time
            if len(times) == 0:
                break

            heapq.heappush(priority_q, first_time)
            heapq.heappush(priority_q, second_time)
            min_time = heapq.heappop(priority_q)
            result += min_time
            times.append(min_time)
            direction *= -1
    return result


def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.

    input = sys.stdin.readline
    T = int(input().rstrip())
    input_data = []
    for _ in range(T):
        N = int(input().rstrip())
        times = deque(map(int, input().split()))
        input_data.append((N, times))

    for i, data in enumerate(input_data, start=1):
        result = find_shortest_time(data[0], data[1])
        print(f'#{i} {result}')


main()
