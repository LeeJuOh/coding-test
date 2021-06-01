def my_solution(n, m, k):
    while k > 0:
        if n >= 2 * m:
            n -= 1
        else:
            m -= 1
        k -= 1
    return min(n // 2, m)


n, m, k = map(int, input().split())
print(my_solution(n, m, k))
