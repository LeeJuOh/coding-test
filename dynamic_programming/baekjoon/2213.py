import sys


def solution(graph, weight):
    global N

    def dfs(node):
        visited[node] = True
        dp[node][0] = 0
        dp[node][1] = weight[node]
        for i in graph[node]:
            if not visited[i]:
                dfs(i)
                dp[node][0] += max(dp[i][0], dp[i][1])
                dp[node][1] += dp[i][0]

    def trace_node(node, case):
        visited[node] = True
        if case:
            trace.append(node)
        for i in graph[node]:
            if not visited[i]:
                # 부모노드를 선택 x, i(자식노들은)
                if dp[i][1] > dp[i][0] and case == 0:
                    trace_node(i, 1)
                # 부모노드를 선택, 자식 선택 불가
                else:
                    trace_node(i, 0)

    visited = [False] * (N + 1)
    dp = [[0] * 2 for _ in range(N + 1)]
    dfs(1)
    result = 0
    case = -1
    if dp[1][0] > dp[1][1]:
        result = dp[1][0]
        case = 0
    else:
        result = dp[1][1]
        case = 1
    visited = [False] * (N + 1)
    trace = []
    trace_node(1, case)
    print(result)
    print(*sorted(trace))


input = sys.stdin.readline
N = int(input().rstrip())
weight = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for i in range(N-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
solution(graph, weight)