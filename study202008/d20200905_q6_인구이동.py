"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 353p
==============================================================================
소요 시간: 해결못함
"""

import sys

input = sys.stdin.readline

# 입력
n, l, r = map(int, input().strip().split())
population = []
for i in range(n):
    temp = list(map(int, input().strip().split()))
    population.append(temp)

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

world = [[0] * n for _ in range(n)]
union_pop = 0
union_count = 0

# 국경선 열기
def open(x, y):
    global union_pop, union_count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if world[x][y] == 0:
        world[x][y] = 1
        union_pop += population[x][y]
        union_count += 1
        for d in range(4):
            diff = abs(world[x][y] - world[x + dx[d]][y + dy[d]])
            if l <= diff <= r:
                open(x + dx[d], y + dy[d])
        return True
    else:
        return False

# 인구 이동
def move():
    set_pop = int(union_pop / union_count)
    for x in range(n):
        for y in range(n):
            if world[x][y] == 1:
                population[x][y] = set_pop

count = 0
for i in range(n * n):
    world = [[0] * n for _ in range(n)]
    union_pop = 0
    union_count = 0
    for x in range(n):
        for y in range(n):
            if world[x][y] == 0:
                open(x, y)
    count += 1

print(count)

"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
개선점: 개선할 수 있는 부분
"""