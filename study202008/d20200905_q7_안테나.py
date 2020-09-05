"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 360p
==============================================================================
소요 시간: 14분
"""

import sys

input = sys.stdin.readline

n = int(input().strip())
house_list = list(map(int, input().strip().split()))
# 먼저 집을 정렬한다.
house_list.sort()

# 집마다 안테나를 설치했을 때의 거리 총합을 저장한다.
case_list = []
for antenar in house_list:
    distance_sum = 0
    for house in house_list:
        distance_sum += abs(antenar - house)
    case_list.append([antenar, distance_sum])

# 거리 순으로 정렬하고 가장 짧은 거리인 안테나 위치를 출력한다.
case_list = sorted(case_list, key=lambda item: item[1])
print(case_list[0][0])

"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
개선점: 개선할 수 있는 부분
"""