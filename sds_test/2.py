import sys
from typing import List
from collections import Counter, deque


def numeric_display(data: List[str], filter: List[str]) -> int:
    # 필터 뒤집어서 사용 가능
    # 필터의 일부가 자리 벗어나면 불가능
    # 숫자 오버, 언더 플로 불가능(0으로 이동 x)
    result = 0
    before_digit = data[0]
    after_digit = data[1]
    filter_size = int(data[2])

    before_digit_size = len(before_digit)
    after_digit_size = len(after_digit)
    if before_digit_size > after_digit_size:
        after_digit = after_digit.zfill(before_digit_size)
    elif before_digit_size < after_digit_size:
        before_digit = before_digit.zfill(after_digit_size)

    before_digit = Counter({i: int(digit) for i, digit in enumerate(before_digit)})
    after_digit = Counter({i: int(digit) for i, digit in enumerate(after_digit)})
    after_digit.subtract(before_digit)

    target = list(after_digit.values())
    print('t', target)
    filter_q = make_digit_filter(filter, len(target))
    print('f', filter_q)
    flag = 0
    # while flag < len(target) - filter_size + 1:
    #     for i in range(len(target)):
    #         if filter_q[i] == 0:
    #         count = target[i] // filter_q[i]
    #         result += abs(count)
    #         target = [x - (y * count) for x, y in zip(target, filter_q)]
    #         filter_q.pop()
    #         filter_q.appendleft(0)
    if not all(d == 0 for d in target) or result == 0:
        result = -1
    return result


def make_digit_filter(filter, target_size):
    q = deque([0] * target_size)
    for i in range(len(filter)):
        ch = filter[i]
        if ch == '+':
            q[i] = 1
        elif ch == '0':
            q[i] = 0
        else:
            q[i] = -1
    return q


def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.

    input = sys.stdin.readline
    T = int(input())
    input_data = []
    input_filters = []
    for _ in range(T):
        input_data.append(list(input().split()))
        input_filters.append(list(input().rstrip()))
    print(input_data, input_filters)

    for i, (data, filter) in enumerate(zip(input_data, input_filters), start=1):
        # print(data, filter)
        result = numeric_display(data, filter)
        print(f'#{i} {result}')
        # break


main()
