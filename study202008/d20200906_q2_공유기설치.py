"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 369p
==============================================================================
소요 시간: 32분
"""

import sys
import math

input = sys.stdin.readline

n, c = map(int, input().strip().split())
houselist = []
for i in range(n):
    houselist.append(int(input().strip()))
    
houselist.sort()
distancelist = [0]
distancesum = 0
for i in range(n):
    if i > 0:
        distance = houselist[i] - houselist[i - 1]
        distancesum += distance
        distancelist.append(distance)

average = round(distancesum / c)

target = average
result = 0
def find(array, start, end):
    global result
    while start <= end:
        mid = (start + end) // 2
        result = mid
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

find(distancelist, 0, len(distancelist) - 1)
print(result)

"""
접근법: 
집의 거리를 따로 저장해두고 거리의 평균을 반올림해서 정수로 만든 뒤,
이진탐색을 돌려서 가장 가까운 mid값을 구하면 그것이 정답이 아닐까 생각했다.

문제에서의 입력 예시는 잘 출력하지만 다른 예시에서도 정답이 나오는지는 잘 모르겠다.
==============================================================================
개선점: 개선할 수 있는 부분
"""