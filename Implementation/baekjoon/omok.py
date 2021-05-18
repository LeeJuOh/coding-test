def my_solution():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            player = board[i][j]
            if player in PLAYER and is_game_over(i, j, player):
                return f'{player}\n{i+1} {j+1}'
    return '0'


def is_game_over(x, y, player):
    for step in steps:
        count = 1
        for i in range(1, WIN_COUNT):
            nx = x + step[0] * i
            ny = y + step[1] * i
            if valid_position(nx, ny) and board[nx][ny] == player:
                count += 1
            else:
                break

            if count == WIN_COUNT and check_over_five_mok(nx, ny, step, player):
                return True
    return False


def valid_position(x, y):
    if x <= -1 or x >= BOARD_SIZE or y <= -1 or y >= BOARD_SIZE:
        return False
    return True


def check_over_five_mok(x, y, step, player):
    directions = [-5, 1]
    for direction in directions:
        nx = x + (step[0] * direction)
        ny = y + (step[1] * direction)
        if valid_position(nx, ny) and board[nx][ny] == player:
            return False
    return True


BOARD_SIZE = 19
WIN_COUNT = 5
PLAYER = (1, 2)
steps = (
    (0, 1), (1, 1),
    (1, 0), (-1, 1)
)
board = []
for _ in range(BOARD_SIZE):
    board.append(list(map(int, input().split())))
print(my_solution())
