def book_solution(n, m, k, l):
    '''
    반복되는 수열 파악
    '''
    ordered_list = sorted(l, reverse=True)
    max_value = ordered_list[0]
    second_max_value = ordered_list[1]

    result = 0
    # 가장 큰 수가더해지는 횟수
    count = (m // (k + 1)) * k + (m % (k + 1))
    result += count * k
    result += (m - count) * second_max_value
    return result


def my_solution(n, m, k, l):
    ordered_list = sorted(l, reverse=True)
    max_value = ordered_list[0]
    second_max_value = ordered_list[1]

    result = 0
    if max_value == second_max_value:
        result = max_value * m
    else:
        while m > 0:
            for _ in range(k):
                if m == 0:
                    return result
                result += max_value
                m -= 1
            result += second_max_value
            m -= 1
    return result


n, m, k = map(int, (input().split()))
l = list(map(int, input().split()))
my_result = my_solution(n, m, k, l)
book_result = book_solution(n, m, k, l)
print(my_result, book_result)
