def my_solution(S):
    count = 0
    i = 0
    size = len(S)
    while i < (size - 1):
        for j in range(i + 1, size):
            if S[i] == S[j] and j < (size - 1):
                continue
            else:
                count += 1
                i = j
                break
    print(count // 2)


def my_solution2(S):
    count = 0
    i = 0
    size = len(S)
    while i < (size - 1):
        for j in range(i + 1, size):
            if S[i] == S[j] and j < (size - 1):
                continue
            else:
                count += 1
                i = j
                break
    print(count // 2)


def book_solution(S):
    count0 = 0      # 전부 0으로 바꾸는 경우
    count1 = 0      # 전부 1로 바꾸는 경우

    if S[0] == '1':
        count0 += 1
    else:
        count1 += 1

    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:
            if S[i + 1] == '1':
                count0 += 1
            else:
                count1 += 1
    print(min(count0, count1))


S = input()
my_solution(S)
book_solution(S)
