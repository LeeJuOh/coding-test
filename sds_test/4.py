from collections import deque
import sys


def lock(N, K, data):
    min_value = sys.maxsize
    for row in data:
        if 0 not in row:
            return 0

    start, end = find_candidate_row(K, data)
    # print('s', start, end)
    # print(data)

    for i in range(start, end+1):
        sum_value = 0
        for j in range(N):
            if data[i][j]:
                continue
            for click in range(1, (K // 2) + 1):
                up = i - click
                if up < 0:
                    up += K
                down = i + click
                if down > K - 1:
                    down %= K
                if data[up][j] == 1 or data[down][j] == 1:
                    sum_value += click
                    break
        if sum_value < min_value:
            min_value = sum_value
    return min_value


def find_candidate_row(K, data):
    window_size = 2
    while True:
        dq = deque()
        start, end = 0, 0
        while start != K - 1:
            dq.append(data[end % K])
            if end >= window_size:
                dq.popleft()
                start += 1
            if len(dq) == window_size and 0 not in [sum(x) for x in zip(*dq)]:
                # print('find', dq)
                # print([sum(x) for x in zip(*dq)])
                return start, (end % K)
            end += 1
            # print(dq)
        window_size += 1


def main():
    input = sys.stdin.readline
    T = int(input().rstrip())
    total_input_data = []
    for _ in range(T):
        input_data = []
        N, K = map(int, input().split())
        for _ in range(K):
            input_data.append(list(map(int, input().rstrip())))
        total_input_data.append((N, K, input_data))

    for i, data in enumerate(total_input_data, start=1):
        # print(data)
        result = lock(data[0], data[1], data[2])
        print(f'#{i} {result}')


main()
