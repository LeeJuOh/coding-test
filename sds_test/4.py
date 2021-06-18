import sys


def lock(N, K, data):
    min_count = sys.maxsize
    lock = [[data[j][i] for j in range(K)] for i in range(N)]
    # print(lock)
    for i in range(K):
        count = 0
        # print(i, "th")
        for j in range(N):
            num = data[i][j]
            # print('num', num)
            if num == 1:
                continue
            for k in range(K // 2):
                left = i - (k + 1)
                right = (i + k + 1) % K
                # print('lock', lock[j])
                # print('left', i, k, lock[j][left])
                # print('right', i, k, lock[j][right])
                if lock[j][left] == 1 or lock[j][right] == 1:
                    count += 1
                    break
        if min_count > count:
            min_count = count
    return min_count


def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.
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
