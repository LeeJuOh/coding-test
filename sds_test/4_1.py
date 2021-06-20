import sys


def lock(N, K, data):
    max_value = -sys.maxsize
    for i in range(K):
        sum_value = sum(data[i])
        if sum_value >= max_value:
            max_value = sum_value
            target = i

    click_count = 0
    for idx, num in enumerate(data[target]):
        if num:
            continue
        for click in range(1, (K // 2) + 1):
            up = target - click
            if up < 0:
                up += K
            down = target + click
            if down > K - 1:
                down %= K
            if data[up][idx] == 1 or data[down][idx] == 1:
                click_count += click
                break
    return click_count


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
        result = lock(data[0], data[1], data[2])
        print(f'#{i} {result}')


main()
