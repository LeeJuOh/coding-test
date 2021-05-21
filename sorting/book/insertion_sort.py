def insertion_sort(array):
    '''
    앞에 정렬된 배열 부분과 비교하며 자신의 위치를 찾아 삽입함으로써 정렬하는 방식
    O(N^2)으로 같은 복잡도이지만 현재 리스트가 거의 정렬되어있다면 O(N)으로 빠르다
    '''
    size = len(array)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break
    return array


def insertion_sort_desc(array):
    '''
    내림차순
    '''
    size = len(array)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if array[j - 1] < array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break
    return array


a = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]
print(insertion_sort(a))
print(insertion_sort_desc(a))
