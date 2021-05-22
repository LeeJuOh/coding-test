# 다이나익 프로그래밍 사용 조건
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
# 퀵 정렬 같은 분할 정복 알고리즘과 달리 다이나믹 프로그래밍은 문제들이 서로 영향을 미치고 있다는 점이다.

def fibo_by_recursion(x):
    '''
    대표 문제, 메모이제이션 기법 사용(탑다운 방식에 국한되어 사용되는 표현, 엄밀히 DP와 별도의 개념)
    >> 한 번 구한 결과를 메모리 공간에 메호해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
    >> 값을 저장하는 방법이므로 캐싱이라고도 한다.
    >> O(N), 일반적으로 재귀 함수는 메모리상의 적재 과정에서의 오버헤드가 있기 때문에 반복문을 이용한 DP가 더 성능이 좋다
    이처럼 재귀함수를 이용하여 DP 소스코드를 작성하는 방법을 top-down 방식 / 하향식
    '''
    # print(f'f({str(x)})')
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo_by_recursion(x - 1) + fibo_by_recursion(x - 2)
    return d[x]


def fibo_by_loop(x):
    '''
    이처럼 작은 문제부터 답을 도출한다고 하여 bottom-up 방식이라고 말한다. / 상향식
    바텀업 방식에서 사용되는 결과 저장용 리스트를 DP table이라고 부른다
    
    '''
    d2[1] = 1
    d2[2] = 1

    for i in range(3, x + 1):
        d2[i] = d2[i - 1] + d2[i - 2]

    return d2[x]


d = [0] * 100
d2 = [0] * 100
print(fibo_by_recursion(6))
print(d)
print(fibo_by_loop(6))
print(d2)
