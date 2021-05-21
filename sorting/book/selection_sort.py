def selection_sort(array):
    '''
    가장 작은 데이터를 찾아서 정렬, O(N^2)
    '''
    size = len(array)
    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


def selection_sort_desc(array):
    '''
    내림차순
    '''
    size = len(array)
    for i in range(size):
        max_idx = i
        for j in range(i + 1, size):
            if array[max_idx] < array[j]:
                max_idx = j
        array[i], array[max_idx] = array[max_idx], array[i]
    return array


a = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]
print(selection_sort(a))
print(selection_sort_desc(a))
