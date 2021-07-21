import sys
from typing import List, Tuple


def solution(hero_atk: int, rooms: List[Tuple[int, int, int]]) -> int:
    max_hp = 0
    need_hp = 0
    dmg = 0
    for type, atk, hp in rooms:
        if type == 1:   # 몬스터
            count, reamin = divmod(hp, hero_atk)
            if reamin == 0:
                count -= 1
            dmg = atk * count
        else:           # 회복
            hero_atk += atk
            dmg = -hp
        need_hp += dmg
        if need_hp < 0:
            need_hp = 0
        max_hp = max(max_hp, need_hp)

    return max_hp + 1


input = sys.stdin.readline
n, hero_atk = map(int, input().split())
rooms = [tuple(map(int, input().split())) for _ in range(n)]
# print(rooms)
print(solution(hero_atk, rooms))