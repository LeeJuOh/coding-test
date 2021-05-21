def my_solution(array):
    sorted_array = sorted(array, reverse=True)
    print(' '.join(map(str, sorted_array)))


n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
my_solution(array)
