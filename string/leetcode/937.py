# 로그파일 재정렬 문제
# 1. 로그의 가장 앞 부분은 식별자
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
# 3. 식별자는 순서에 영향 x, 동일 문자일 경우 식별자 순
# 4. 숫자 로그는 입력 순서


from typing import List


def reorder_log_files(logs: List[str]) -> List[str]:
    # 람다와 연산자 사용
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    print(digits)
    print(letters)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    print(letters)

    return letters + digits


logs = ["digit1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reorder_log_files(logs))
