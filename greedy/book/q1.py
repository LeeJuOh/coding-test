def my_solutuion(n, data):
    result = 0
    group_count = 0
    sorted_data = sorted(data)
    for fear in sorted_data:
        group_count += 1
        if group_count >= fear:
            result += 1
            group_count = 0
    print(result)


n = int(input())
data = list(map(int, input().split()))
my_solutuion(n, data)
