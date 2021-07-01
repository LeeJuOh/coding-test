import sys
from typing import List
from bisect import bisect_left, bisect_right


def solution(target: int, class_size: int, studnets: List[List[int]]) -> int:
    global CLASS_COUNT
    array = [0] * class_size
    for i in range(class_size):
        for student in studnets:
            array[i] += student[i]
    # print(array)
    left_idx = bisect_left(array, target)
    right_idx = bisect_right(array, target)
    if left_idx == 0 and right_idx == 0:
        return array[left_idx]
    elif left_idx != right_idx:
        return array[left_idx]
    elif left_idx == class_size and right_idx == class_size:
        return array[class_size - 1]
    left_idx = right_idx - 1

    answer = -target
    sum_value = 0
    for i in range(left_idx, right_idx + 1):
        for j in range(left_idx, right_idx + 1):
            for k in range(left_idx, right_idx + 1):
                for l in range(left_idx, right_idx + 1):
                    sum_value = students[0][i] + students[1][j] + \
                                students[2][k] + students[3][l]
                    if (abs(target - sum_value) < abs(target - answer)) or \
                       (abs(target - sum_value) == abs(target - answer) and sum_value < answer):
                        answer = sum_value
    return answer


input = sys.stdin.readline
T = int(input().rstrip())
CLASS_COUNT = 4
result = []
for _ in range(T):
    TARGET, CLASS_SIZE = map(int, input().split())
    students = [sorted(list(map(int, input().split()))) for _ in range(CLASS_COUNT)]
    # print(students)
    result.append(solution(TARGET, CLASS_SIZE, students))

for x in result:
    print(x)
