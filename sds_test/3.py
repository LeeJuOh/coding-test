from collections import deque
import sys


def rush_hour(data):
    board = [[0] * 5 for _ in range(5)]
    car_map = {}
    start = (0, 0)
    HORIZON = 1
    VERITICAL = -HORIZON
    horizon = [(0, 1), (0, -1)]
    veritical = [(1, 0), (-1, 0)]
    for i, car in enumerate(data, start=1):
        x, y = int(car[0]) - 1, int(car[1]) - 1
        direction = car[2]
        if i == 0:
            start = (x, y)

        board[x][y] = i
        if direction == 'E':
            board[x][y-1] = i
            car_map[i] = HORIZON
        elif direction == 'W':
            board[x][y+1] = i
            car_map[i] = HORIZON
        elif direction == 'N':
            board[x+1][y] = i
            car_map[i] = VERITICAL
        else:
            board[x-1][y] = i
            car_map[i] = VERITICAL

    for i in range(5):
        for j in range(5):
            print(board[i][j], end=' ')
        print('')

    q = deque()
    q.append(1)

    candidate = []
    for i in range(start[0] + 1, 5):
        if board[2][i] > 1:
            candidate.append(board[][])





    
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
