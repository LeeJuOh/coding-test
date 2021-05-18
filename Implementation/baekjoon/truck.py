from collections import deque


def my_solution(W, L, trucks):
    bridge = deque([0 for _ in range(W)])
    current_weight = 0
    time = 0
    while trucks:
        current_weight -= bridge.popleft()
        if current_weight + trucks[0] <= L:
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
        time += 1
    time += W
    print(time)


N, W, L = map(int, input().split())
trucks = deque(map(int, input().split()))
my_solution(W, L, trucks)
