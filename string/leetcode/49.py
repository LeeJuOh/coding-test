from collections import defaultdict
from typing import List

# 그룹 애너그램
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라


def group_anagrams(strs: List[str]) -> List[str]:
    anagrams = defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
