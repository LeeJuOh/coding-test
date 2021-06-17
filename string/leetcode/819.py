import re
# from collections import defaultdict
from typing import Counter, List

# 가장 흔한 단어 문제
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
# 대소문자 구분 x
# 구두점(마침표, 쉼표) 또한 무시한다.


def most_common_word(paragraph: str, banned: List[str]) -> str:
    # 데이터 클렌징이라 부르는 입력값에 대한 전처리 작업이 필요
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
             if word not in banned]
    print(words)
    # counts = defaultdict(int)
    # for word in words:
    #     counts[word] += 1
    # return max(counts, key=counts.get)

    counts = Counter(words)
    return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(most_common_word(paragraph, banned))
