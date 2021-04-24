def my_solution(n, m):
    result = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        min_value = min(row)
        result = max(result, min_value)
    return result

def book_solution_1(n, m):
    my_solution(n, m)

def book_solution_2(n, m):
    result = 0
    for i in range(n):
        data = list(map(int, input().split()))
        min_value = 10001
        for a in data:
            min_value = min(min_value, a)
        result = max(result, min_value)
    return result

n, m = map(int, (input().split()))
my_result = my_solution(n, m)
book_result = book_solution_2(n, m)
print(my_result, book_result, my_result==book_result)