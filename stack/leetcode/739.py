# 일일 온도
# 매일의 화씨 온도 리스트 T를 받아서
# 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지 출력

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    stack = []
    answer = [0] * len(temperatures)
    for i, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer