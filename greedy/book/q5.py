import time


def my_solution(N, M, balls):
    result = 0
    ball_counts = [0] * (M + 1)
    for ball in balls:
        ball_counts[ball] += 1

    for i in range(1, M + 1):
        for j in range(i + 1, M + 1):
            result += (ball_counts[i] * ball_counts[j])


# 총 볼 개수에서 해당 공의 갯수를 뺌으로써 나머지 공의 개수를 알 수 있음
# 시간 복잡도가 O(N)으로 감소
def book_solution(N, M, balls):
    result = 0
    ball_counts = [0] * (M + 1)
    for ball in balls:
        ball_counts[ball] += 1

    for i in range(1, M + 1):
        N -= ball_counts[i]
        result += (ball_counts[i] * N)


N, M = map(int, input().split())
balls = list(map(int, input().split()))

start_time = time.time()
my_solution(N, M, balls)
end_time = time.time()
print('time :', end_time - start_time)

start_time = time.time()
book_solution(N, M, balls)
end_time = time.time()
print('time :', end_time - start_time)
