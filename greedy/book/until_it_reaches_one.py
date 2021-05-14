def my_solution(n, k):
    result = 0
    while n > 1:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        result += 1
    return result


def book_solution(n, k):
    '''
    n이 k의 배수가 되도록 한 번에 빼는 방식
    '''
    result = 0

    while True:
        target = (n // k) * k
        result += (n - target)
        n = target
        if n < k:
            break
        result += 1
        n //= k

    result += (n - 1)
    return result


n, k = map(int, (input().split()))
my_result = my_solution(n, k)
book_result = book_solution(n, k)
print(my_result, book_result, my_result == book_result)
