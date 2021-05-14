def my_solution(n, k, coins):
    result = 0
    for coin in coins[::-1]:
        if k == 0:
            break
        result += k // coin
        k %= coin
    return result


n, k = map(int, (input().split()))
coins = [int(input()) for _ in range(n)]
print(str(my_solution(n, k, coins)))
