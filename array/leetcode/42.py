# 빗물 트래핑
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산
# 너무 어렵다..


from typing import List


def rain_trap_by_two_point(height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1

        else:
            volume += right_max - height[right]
            right -= 1
    return volume


def rain_trap_by_stack(height: List[int]) -> int:
    # 높이가 꺾이는 변곡점을 기준으로 격차만큼 물 높이 volume을 채운다.

    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * waters
        stack.append(i)
    return volume


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(rain_trap_by_two_point(height))
print(rain_trap_by_stack(height))