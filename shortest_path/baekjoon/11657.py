import sys
from typing import List, Tuple


# 밸만-포드 알고리즘
# 정점 - 1 횟수만큼 모든 간선의 edge relaxation 수행
# edge relaxation:
#   모든 간선들을 탐색하면서,
#   간선이 잇는 출발정점이 '한번이라도 계산 된 정점'
#   이라면 해당 간선이 잇는 정점의 거리를 비교해서 업데이트
# 그리고 한번 더 edge relaxation
# 순환할수록 무한히 가중치가 작아지는 음의 사이클이 없다면 값이 변하지 않는다
# 있다면 값이 변한다, 사이클 판단 가능
def solution(n: int, edges: List[Tuple[int, int, int]]) -> None:
    INF = int(1e9)
    dist = [INF] * (N + 1)
    dist[1] = 0
    for _ in range(N - 1):
        for start, end, cost in edges:
            if dist[start] != INF and dist[start] + cost < dist[end]:
                dist[end] = dist[start] + cost

    # 순환할수록 무한히 가중치가 작아지는 음의 사이클 판단
    is_cycle = False
    for start, end, cost in edges:
        if dist[start] != INF and dist[start] + cost < dist[end]:
            is_cycle = True
    if is_cycle:
        print(-1)
    else:
        for d in dist[2:]:
            print(-1 if d == INF else d)


input = sys.stdin.readline
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
solution(N, edges)
