import sys
from typing import List


def numeric_display(data: List[str], filter: List[str]) -> int:
    # 필터 뒤집어서 사용 가능
    # 필터의 일부가 자리 벗어나면 불가능
    # 숫자 오버, 언더 플로 불가능(0으로 이동 x)
    result = 0
    before = list(map(int, data[0].zfill(6)))
    after = list(map(int, data[1].zfill(6)))
    size = int(data[2])
    # print(before, after, size)
    filters = get_filter(filter)
    # print('filter', filters)

    for i in range(6 - size + 1):
        # print('b', before[i:i + size])
        # print('a', after[i:i + size])
        count = 0
        for filter, idx in filters:
            # print(filter, idx)
            difference = after[i:i + size][idx] - before[i:i + size][idx]
            if (difference > 0 and filter[idx]) > 0 or (difference < 0 and filter[idx] < 0):
                count = (after[i:i + size][idx] - before[i:i + size][idx]) // filter[idx]
                before[i:i + size] = [x + f * count for x, f in zip(before[i:i + size], filter)]
                result += count
                # print(count, before)
    # print('finishi', before, after)
    if not before == after or result == 0:
        result = -1
    return result


def get_filter(filter):
    filters = []
    for f in [filter, reversed(filter)]:
        temp = []
        main_filter_idx = None
        for i, ch in enumerate(f):
            if ch == '+':
                temp.append(1)
            elif ch == '0':
                temp.append(0)
            else:
                temp.append(-1)

            if main_filter_idx is None and ch != '0':
                main_filter_idx = i
        filters.append([temp, main_filter_idx])
    return filters


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
    # print(input_data, input_filters)

    for i, (data, filter) in enumerate(zip(input_data, input_filters), start=1):
        # print(data, filter)
        result = numeric_display(data, filter)
        print(f'#{i} {result}')
        # break


main()
