def my_soultion(m, array):
    start = 0
    end = max(array)
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for item in array:
            if item > mid:
                total += item - mid
        
        if total >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1  
    print(result)


n, m = map(int, input().split())
array = list(map(int, input().split()))
my_soultion(m, array)
