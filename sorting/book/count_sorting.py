def count_sort(array):
    '''
    데이터를 비교하며 정렬하는 비교 기반의 정렬 알고리즘이 아니다.
    데이터의 크기 범위가 제한 되어 정수 형태로 표현할 수 있을 때 사용하는 정렬
    일반적으로 데이터의 차이가 1,000,000을 넘지 않을 때 효과적
    O(N + K)를 보장하여 빠르다
    N: 데이터의 개수
    K: 데이터 중 최대값
    '''
    
    count = [0] * (max(array) + 1)
    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


def count_sort_desc(array):
    '''
    내림차순
    '''
    count = [0] * (max(array) + 1)
    for i in range(len(array)):
        count[array[i]] += 1

    for i in reversed(range(len(count))):
        for j in range(count[i]):
            print(i, end=' ')


a = [4, 3, 5, 7, 9]
count_sort(a)
print('\n')
count_sort_desc(a)
print('\n')
