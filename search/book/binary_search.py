def binary_search_by_recursion(array, target, start, end):
    '''
    시간 복잡도: O(logN), 배열 내부의 데이터가 정렬되어 있어야 한다.
    탐색 범위가 큰 상황에서의 가정하는 문제에 주로 사용
    탐색 범위가 2,000만을 넘어가면 이진 탐색으로 접근 권장,
    데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 
    logN 속도를 내야하는 알고리즘을 떠올리자
    '''
    if start > end:
        return None

    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_by_recursion(array, target, start, mid - 1)
    else:
        return binary_search_by_recursion(array, target, mid + 1, end)


def binary_search_by_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search_by_recursion(array, target, 0, n - 1)
if result:
    print(result + 1)
else:
    print('원소가 존재하지 않습니다.')

result = binary_search_by_loop(array, target, 0, n - 1)
if result:
    print(result + 1)
else:
    print('원소가 존재하지 않습니다.')