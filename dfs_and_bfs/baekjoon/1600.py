import sys
from collections import deque


def solution(x, y, horse_count, distance):
    global W, H

    def is_valid(x: int, y: int) -> bool:
        global W, H

        if x < 0 or y < 0 or x >= H or y >= W:
            return False
        return True

    def move(move_dx, move_dy, horse_count, distance, type=None):
        for dx, dy in zip(move_dx, move_dy):
            nx = x + dx
            ny = y + dy

            if type == 'horse':
                horse_count += 1

            if is_valid(nx, ny) and board[nx][ny] == 0 and \
               not visited[nx][ny][horse_count]:
                queue.append((nx, ny, horse_count, distance + 1))
                visited[nx][ny][horse_count] = True

    board = []
    for _ in range(H):
        board.append(list(map(int, input().split())))
    horse_dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    horse_dy = [-2, -1, 1, 2, -2, -1, 1, 2]
    monkey_dx = [0, -1, 0, 1]
    monkey_dy = [-1, 0, 1, 0]

    queue = deque()
    queue.append((x, y, horse_count, distance))
    visited = [[[False] * 31 for _ in range(W)] for _ in range(H)]
    print(len(visited))
    print(len(visited[0]))
    print(len(visited[0][0]))
    while queue:
        x, y, horse_count, distance = queue.popleft()
        if x == H - 1 and y == W - 1:
            return distance

        if horse_count < K:
            move(horse_dx, horse_dy, horse_count, distance, 'horse')
        move(monkey_dx, monkey_dy, horse_count, distance)
    return -1


input = sys.stdin.readline
K = int(input().rstrip())
W, H = map(int, input().split())
print(solution(0, 0, 0, 0))
