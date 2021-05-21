def quick_sort(array, start, end):
    '''
    기준 데이터인 피벗을 이용해 큰 데이터와 작은데이터의 위치를 변경하면서 정렬하는 방식
    O(NlogN)으로 같은 복잡도로 병합 정렬 알고리즘과 같이 빠른 정렬 알고리즘
    '''
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1

        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


def quick_sort_desc(array, start, end):
    '''
    내림차순
    '''
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] >= array[pivot]):
            left += 1
        while(right > start and array[right] <= array[pivot]):
            right -= 1

        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort_desc(array, start, right - 1)
    quick_sort_desc(array, right + 1, end)


a = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(a, 0, len(a) - 1)
print(a)
quick_sort_desc(a, 0, len(a) - 1)
print(a)
