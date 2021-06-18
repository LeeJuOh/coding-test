import sys
import heapq
from itertools import combinations
from typing import List


def find_shortest_time(N: int, times: List[int]) -> int:
    result = 0
    if len(times) == 1:
        result = times[0]
    else:

        priority_q = []
        time_map = {i: time for i, time in enumerate(times)}
        while True:
            pairs = list(combinations(time_map.keys(), 2))
            min_value = sys.maxsize
            x, y = -1, -1
            for i, j in pairs:
                abs_value = abs(time_map[i] - time_map[j])
                if abs_value < min_value:
                    min_value = abs_value
                    x, y = i, j

            result += time_map[x] if time_map[x] >= time_map[y] else time_map[y]
            heapq.heappush(priority_q, (time_map[x], x))
            heapq.heappush(priority_q, (time_map[y], y))
            del time_map[x]
            del time_map[y]

            if not time_map:
                break

            return_time, key = heapq.heappop(priority_q)
            result += return_time
            time_map[key] = return_time
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
        times = list(map(int, input().split()))
        input_data.append((N, times))

    for i, data in enumerate(input_data, start=1):
        result = find_shortest_time(data[0], data[1])
        print(f'#{i} {result}')


main()
