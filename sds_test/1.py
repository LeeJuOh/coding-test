import heapq
import sys
from collections import deque
from typing import List


def moving_camels(N: int, camles: List[int]) -> int:
    result = 0
    if len(camles) == 1:
        result = camles[0]
    else:
        opposite_queue = []
        direction = 1
        first_time = 0
        second_time = 0
        return_time = 0
        while True:
            camles = deque(sorted(camles))
            if direction == 1:
                first_time = camles.popleft()
                second_time = camles.popleft()
            else:
                second_time = camles.pop()
                first_time = camles.pop()
            result += second_time
            if not camles:
                break

            heapq.heappush(opposite_queue, first_time)
            heapq.heappush(opposite_queue, second_time)
            return_time = heapq.heappop(opposite_queue)
            result += return_time
            camles.append(return_time)
            direction *= -1
    return result


def main():
    input = sys.stdin.readline
    T = int(input().rstrip())
    total_input = []
    for _ in range(T):
        N = int(input().rstrip())
        camles = list(map(int, input().split()))
        total_input.append((N, camles))

    for i, data in enumerate(total_input, start=1):
        result = moving_camels(data[0], data[1])
        print(f'#{i} {result}')


main()
