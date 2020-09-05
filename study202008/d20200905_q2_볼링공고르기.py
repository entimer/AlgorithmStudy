"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 315p
==============================================================================
소요 시간: 25분
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
balls = list(map(int, input().rstrip().split()))

weights = [0] * (m + 1)
for ball in balls:
    weights[ball] += 1

count = 0
ball_count = n
for weight in weights:
    ball_count -= weights[weight]
    count += ball_count * weights[weight]

print(count)

"""
접근법: 
1. 공을 무게별로 몇개가 있는지를 먼저 저장한다.
2. 가장 무게가 낮은 공부터 1번이 꺼내고 그보다 높은 무게의 공을 2번이 드는 경우의 수를 카운트한다.
3. 현재 1번이 꺼낸 무게의 공을 공 갯수에서 제외한다.
4. 끝날 때 까지 2번으로 돌아간다.
==============================================================================
개선점: 개선할 수 있는 부분
"""