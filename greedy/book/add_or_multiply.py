
def my_solution(str):
    result = 0
    for num in str:
        num = int(num)
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    print(result)


str = input()
my_solution(str)
