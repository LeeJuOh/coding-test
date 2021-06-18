import sys


def rush_hour(data):
    board = [[0] * 5 for _ in range(5)]
    for car in data:
        i, j = int(car[0]) - 1, (car[1]) - 1

    count = 0
    return count


def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.
    input = sys.stdin.readline
    T = int(input())
    total_input = []
    for _ in range(T):
        input_data = []
        N = int(input().rstrip())
        for _ in range(N):
            input_data.append(list(input().split()))
        total_input.append(input_data)
    for i, data in enumerate(total_input):
        print(data)
        result = rush_hour(data)
        print(f'#{i} {result}')

main()