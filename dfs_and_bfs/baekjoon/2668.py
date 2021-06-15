def dfs(node):
    next_node = array[node]
    if not visited[next_node]:
        parent[next_node] = node
        dfs(next_node)
    elif
    finished[node] = True


def find_cycle_node(node, next_node):
    if node != next_node:
        result.append(node)
        print(result)
        find_cycle_node(parent[node], next_node)


N = int(input())
array = [int(input()) for _ in range(N)]
array.insert(0, 0)
visited = [False] * (N + 1)
finished = [False] * (N + 1)
parent = [i for i in range(N + 1)]

result = []
for i in range(1, N + 1):
    dfs(i, i)
print(len(result))
for i in sorted(result):
    print(i)
