def my_solution(array):
    sorted_array = sorted(array, key=lambda student: student[1])
    for student in sorted_array:
        print(student[0], end=' ')


n = int(input())
array = []
for i in range(n):
    input_date = input().split()
    array.append((input_date[0], int(input_date[1])))
my_solution(array=array)
