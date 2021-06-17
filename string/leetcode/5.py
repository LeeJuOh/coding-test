# 가장 긴 팰린드롬 부분 문자열
# 가장 긴 팰린드롬 부분 문자열을 출력하라


def longest_palindrome(s: str) -> str:
    # 최장 공통 부분 문자열이라는 문제가 있다.
    # 위의 문제는 다이나믹 프로그래밍으로 풀 수 있는 전형적인 문제
    # 해당 문제 또한 동일한 유형의 문제로서, 동일하게 dp로 풀 수 있지만
    # 성능이 느리고 직관적이지 않고 팰린드롬 관별만 하면 된다는 점을 착안해
    # 투포인트를 슬라이딩 윈도우처럼 이용

    def expand(left: int, right: int) -> str:
        while left > 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            print('expand')
        print(left, right, s)
        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result


s = "a123454321"
s2 = "cbbd"
print(longest_palindrome(s))
print(longest_palindrome(s2))