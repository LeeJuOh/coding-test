def my_solution(n, p):
    sorted_times = sorted(p)
    result = 0
    waiting_time = 0
    for i in range(n):
        result += waiting_time + sorted_times[i]
        waiting_time += sorted_times[i]
    return result


n = int(input())
p = list(map(int, input().split()))
print(str(my_solution(n, p)))
