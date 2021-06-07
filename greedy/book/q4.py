# 개념적으로 이해하기 까다로운 문제였다.

def my_solution(N, coins):
    coins.sort()
    amount = 1
    for coin in coins:
        if amount < coin:
            break
        amount += coin
    print(amount)


N = int(input())
coins = list(map(int, input().split()))
my_solution(N, coins)
