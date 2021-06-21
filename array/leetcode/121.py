# 주식을 사고팔기 가장 좋은 시점
# 한 번의 거래로 낼 수 있는 최대 이익 산출하라

import sys
from typing import List


def max_profit(prices: List[int]) -> int:
    # 저점과 현재 값과의 차이를 계산하면서 최대값을 계속 교체하는 방식
    # 최대 서브 배열 문제의 답인 카데인 알고리즘과 비슷
    # O(n)
    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit
