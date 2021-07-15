import sys
from typing import List


def solution(row: int, col: int) -> None:
    def direction(s: str) -> List[int]:
        # 상 하
        if s == '|':
            return [0, 1]
        # 좌 우
        elif s == '-':
            return [2, 3]
        # 상 하 좌 우
        elif s == '+' or s == 'M' or s == 'Z':
            return [0, 1, 2, 3]
        # 하 우
        elif s == '1':
            return [1, 3]
        # 상 우
        elif s == '2':
            return [0, 3]
        # 상 좌
        elif s == '3':
            return [0, 2]
        # 하 좌
        elif s == '4':
            return [1, 2]


    def isValid(x: int, y: int) -> bool:
        return 0 <= x and x < row and 0 <= y and y < col

    graph = [list(input().rstrip()) for _ in range(row)]
    print(graph)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for i in range(row):
        for j in range(col):
            node = graph[i][j]
            if node == 'M':
                start_x, start_y = i, j
            elif node == 'Z':
                end_x, end_y = i, j



input = sys.stdin.readline
row, col = map(int, input().split())
print(solution(row, col))
