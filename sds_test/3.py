from collections import deque
import sys


def main():
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
        result = rush_hour(data)
        print(f'#{i} {result}')


def rush_hour(data):
    global HORIZON, VERTICAL
    board = [[0] * 5 for _ in range(5)]
    car_map = {}
    start_x, start_y = 0, 0

    horizon = [(0, 1), (0, -1)]
    veritical = [(1, 0), (-1, 0)]
    for i, car in enumerate(data, start=1):
        x, y = int(car[0]) - 1, int(car[1]) - 1
        direction = car[2]
        if i == 1:
            start_x, start_y = x, y

        board[x][y] = i
        if direction == 'E':
            board[x][y-1] = i
            car_map[i] = HORIZON
        elif direction == 'W':
            board[x][y+1] = i
            car_map[i] = HORIZON
        elif direction == 'N':
            board[x+1][y] = i
            car_map[i] = VERTICAL
        else:
            board[x-1][y] = i
            car_map[i] = VERTICAL

    seq = set()
    q = deque()
    q.append((1, start_x, start_y))
    while q:
        now, x, y = q.popleft()
        direction = car_map.get(now)
        if direction == HORIZON:
            search_dir = horizon
        else:
            search_dir = veritical
        for dir in search_dir:
            i = 1
            while True:
                nx = x + dir[0] * i
                ny = y + dir[1] * i
                if not is_valid_position(nx, ny):
                    break
                car = board[nx][ny]
                if car not in [0, now] and is_valid_car(direction, car_map[car]):
                    car = board[nx][ny]
                    q.append([car, nx, ny])
                i += 1
        seq.add(now)
    return -1


def is_valid_position(x, y):
    if x < 0 or y < 0 or x > 4 or y > 4:
        return False
    return True


def is_valid_car(current_direction, car_direction):
    global HORIZON, VERTICAL
    if current_direction * car_direction == -1:
        return True
    return False


HORIZON = 1
VERTICAL = -HORIZON
main()
