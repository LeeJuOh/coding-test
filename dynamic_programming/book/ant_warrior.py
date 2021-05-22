def my_solution(n, array):
    d[0] = array[0]
    d[1] = max(array[0], array[1])

    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])
    print(d[n - 1])
    print(d)


n = int(input())
d = [0] * 100
array = list(map(int, input().split()))
my_solution(n, array)
