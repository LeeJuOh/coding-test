import sys
from collections import deque


def solution(x, y, horse_count, distance):
    global W, H

    def move(move_dx, move_dy, horse_count, distance, type=None):
        for dx, dy in zip(move_dx, move_dy):
            nx = x + dx
            ny = y + dy
            if nx == H - 1 and ny == W - 1:
                return True
            if not is_valid(nx, ny) or board[nx][ny] == 1 or visited[distance][nx][ny]:
                continue

            if type == 'horse':
                horse_count += 1
            queue.append((nx, ny, horse_count, distance + 1))

        return False

    board = []
    for _ in range(H):
        board.append(list(map(int, input().split())))
    horse_dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    horse_dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    monkey_dx = [0, -1, 0, 1]
    monkey_dy = [-1, 0, 1, 0]

    queue = deque()
    queue.append((x, y, horse_count, distance))
    visited = [[[False] * W for _ in range(H)] for _ in range(32)]
    # print(len(visited))
    # print(len(visited[0]))
    # print(len(visited[0][0]))
    flag1 = False
    flag2 = False
    while queue:
        x, y, horse_count, distance = queue.popleft()
        visited[distance][x][y] = True

        if horse_count < K:
            flag1 = move(horse_dx, horse_dy, horse_count, distance, 'horse')
        flag2 = move(monkey_dx, monkey_dy, horse_count, distance)
        if flag1 or flag2:
            return distance
    return -1


def is_valid(x: int, y: int) -> bool:
    global W, H

    if x < 0 or y < 0 or x >= H or y >= W:
        return False
    return True


input = sys.stdin.readline
K = int(input().rstrip())
W, H = map(int, input().split())
print(solution(0, 0, 0, 0))
