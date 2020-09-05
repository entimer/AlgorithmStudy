"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 351p
==============================================================================
소요 시간: 62분
"""

import sys
from itertools import combinations

input = sys.stdin.readline

# 선생, 학생 위치 리스트
teacherlist = []
studentlist = []
emptylist= []

n = int(input().strip())
schoolmap = []
for x in range(n):
    temp = list(map(str, input().strip().split()))
    schoolmap.append(temp)
    # 학생과 선생님 위치 저장
    for y in range(len(temp)):
        something = temp[y]
        if something == 'T':
            teacherlist.append([x, y])
        elif something == 'S':
            studentlist.append([x, y])
        else:
            emptylist.append([x, y])

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 학생 찾기
def find(x, y, d, newmap):
    if d == 0:
        while y >= 0:
            if newmap[x][y] == 'O':
                return False
            if newmap[x][y] == 'S':
                return True
            y -= 1
    if d == 1:
        while x < n:
            if newmap[x][y] == 'O':
                return False
            if newmap[x][y] == 'S':
                return True
            x += 1
    if d == 2:
        while y < n:
            if newmap[x][y] == 'O':
                return False
            if newmap[x][y] == 'S':
                return True
            y += 1
    if d == 3:
        while x >= 0:
            if newmap[x][y] == 'O':
                return False
            if newmap[x][y] == 'S':
                return True
            x -= 1

# 빈 자리에 장애물을 설치하는 경우의 수
obstacle_cases = list(combinations(emptylist, 3))
print(obstacle_cases)

def check(case, newmap):
    for teacher in teacherlist:
        for direction in range(4):
            if find(teacher[0], teacher[1], direction, newmap):
                return True
    return False

isdanger = False
for case in obstacle_cases:
    # 매 경우마다 맵을 복사해서 장애물 설치
    newmap = schoolmap[:]
    for obstacle in case:
        ox = obstacle[0]
        oy = obstacle[1]
        newmap[ox][oy] = 'O'
    if not check(case, newmap):
        isdanger = True

if isdanger:
    print("YES")
else:
    print("NO")


"""
접근법: 경우의 수가 얼마 없으니까 장애물 설치하는 모든 경우의 수를 구해서 각각 체크한다.
==============================================================================
개선점: 개선할 수 있는 부분
"""