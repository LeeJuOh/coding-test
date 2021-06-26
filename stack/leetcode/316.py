# 중복 문자 제거
# 중복된 문자를 제외하고 사전식 순서로 나열하라
# bcabc -> abc
# ebcabc -> eabc
# cbacdcbc -> acdb
# 문제 이해가 안된다..


from typing import Counter


def remove_duplicate_letters_by_recursive(s: str) -> str:
    print(sorted(set(s)))
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        print(suffix)
        if set(s) == set(suffix):
            return char + remove_duplicate_letters_by_recursive(suffix.replace(char, ''))
    return ''


def remove_duplicate_letters_by_stack(s: str) -> str:
    counter, seen, stack = Counter(s), set(), []
    print(counter)
    for char in s:
        counter[char] -= 1
        if char in stack:
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    return ''.join(stack)


s = "cbacdcbc"
print(remove_duplicate_letters_by_recursive(s))
print(remove_duplicate_letters_by_stack(s))