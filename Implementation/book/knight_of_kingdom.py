def my_solution(input_data):
    MIN_VALUE = 1
    MAX_VALUE = 8
    steps = [
        (1, 2), (-1, 2),
        (1, -2), (-1, -2),
        (-2, -1), (-2, 1),
        (2, -1), (2, 1),
    ]

    x = int(input_data[1])
    # ord : str to ascii, chr: ascii to str
    y = int(ord(input_data[0]) - ord('a')) + 1
    result = 0
    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        if nx >= MIN_VALUE and nx <= MAX_VALUE and \
           ny >= MIN_VALUE and ny <= MAX_VALUE:
            result += 1
    return result


input_data = input()
print(my_solution(input_data))
