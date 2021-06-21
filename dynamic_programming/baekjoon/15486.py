import sys


def my_solution(N, T, P):
    dp = [0] * (N + 1)
    max_value = 0
    for i in range(N):
        max_value = max(max_value, dp[i])
        if i + T[i] > N:
            continue
        dp[i+T[i]] = max(max_value + P[i], dp[i+T[i]])
    return max(max_value, dp[N])


input = sys.stdin.readline
N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
print(my_solution(N, T, P))