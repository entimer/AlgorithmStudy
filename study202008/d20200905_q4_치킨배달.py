"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 332p
==============================================================================
소요 시간: 38분
"""

import sys
from itertools import combinations

input = sys.stdin.readline

# 입력
n, m = map(int, input().strip().split())

# 집과 치킨집의 좌표들을 저장해둘 리스트
houses = []
chickens = []

# 도시 정보 입력
city = [[0] * (n + 1)]
for i in range(n):
    temp = list(map(int, input().strip().split()))
    temp.insert(0, 0)
    city.append(temp)
    # 집과 치킨집의 좌표를 저장
    for index in range(len(temp)):
        if temp[index] == 1:
            houses.append([i, index])
        if temp[index] == 2:
            chickens.append([i, index])

# 거리를 구하는 함수
def get_distance(start, end):
    sx = start[0]
    sy = start[1]
    ex = end[0]
    ey = end[1]
    return abs(sx - ex) + abs(sy - ey)

# 치킨거리를 구하는 함수(집과 가장 가까운 치킨집)
def get_chicken_distance(house, chickens):
    mininum = 100000
    for chicken in chickens:
        dis = get_distance(house, chicken)
        mininum = min(mininum, dis)
    return mininum

# 치킨집 중 m개의 치킨집을 고르는 모든 경우의 수를 저장
combi = list(combinations(chickens, m))

# 도시의 치킨거리 리스트
city_distance_list = []

# 각 경우의 수마다
for c in combi:
    # 각 집마다 치킨거리를 구해서 도시의 치킨거리에 더하고
    city_distance = 0
    for house in houses:
        city_distance += get_chicken_distance(house, c)
    # 도시의 치킨거리 리스트에 저장
    city_distance_list.append(city_distance)

# 도시의 치킨거리 리스트 중 최솟값 출력
print(min(city_distance_list))
        
"""
접근법: 
모든 치킨집 중 m개의 치킨집을 구하는 경우의 수를 리스트로 저장해두고
각 경우의 수마다, 도시의 치킨거리를 구해서
마지막에 그 최솟값을 구하면 m개의 치킨집만 남겼을 때의 도시의 치킨거리 최솟값이 나온다.

마침 경우의 수를 구할 수 있는 모듈이 파이썬에 있었다. from itertools import combinations
따라서 list(combinations(chickens, m))로 경우의 수를 리스트로 받아두고
경우의 수마다 도시의 치킨거리를 0으로 만들고, 치킨거리들을 구해서 더한 다음, 따로 리스트에 저장한다.
그 후 리스트의 최솟값을 출력했다.
==============================================================================
개선점: 개선할 수 있는 부분
"""