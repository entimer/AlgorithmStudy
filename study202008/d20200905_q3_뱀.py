"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 327p
==============================================================================
소요 시간: 70분
"""

import sys
input = sys.stdin.readline

# 입력부
n = int(input().strip())
k = int(input().strip())

# 게임 맵
gamemap = [[0] * (n + 1) for _ in range(n + 1)]

# 사과 위치 표시
for i in range(k):
    posx, posy = map(int, input().strip().split())
    gamemap[posx][posy] = 1

# 회전 정보
l = int(input().strip())
turns = {}
for i in range(l):
    x, c = map(str, input().strip().split())
    turns[int(x)] = c

# 방향에 따른 이동값(동남서북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 현재 머리 위치
headx, heady = 1, 1
# 뱀이 차지하는 영역
gamemap[headx][heady] = -1
# 뱀 정보
snake = [headx, heady]
# 뱀의 현재 진행방향(0: 동, 1: 남, 2: 서, 3: 북)
curdir = 0
# 현재 게임 시간
time = 0

def printmap():
    print(time, curdir, headx, heady)
    for x in range(1, n + 1):
        print(gamemap[x])

# 시뮬레이션
while(True):
    printmap()
    # 다음 위치 저장
    nextx = headx + dx[curdir]
    nexty = heady + dy[curdir]
    print(nextx, nexty, dx[curdir])
    # 다음위치 유효성 검사
    if nextx < 1 or nextx > n or nexty < 1 or nexty > n:
        time += 1
        break
    # 다음 위치가 몸통인지 검사
    if gamemap[nextx][nexty] == -1:
        time += 1
        break
    # 다음 위치가 사과라면 이동 후 꼬리 유지
    if gamemap[nextx][nexty] == 1:
        snake.append([nextx, nexty])
    # 다음 위치가 사과가 아니라면 이동 후 꼬리 제거
    else:
        snake.append([nextx, nexty])
        tail = snake.pop()
        gamemap[tail[0]][tail[1]] = 0
    headx, heady = nextx, nexty
    gamemap[headx][heady] = -1
    
    # 시간 1 증가
    time += 1
    # 회전
    if time in turns:
        turn = turns[time]
        print(turn)
        if turn == 'D':
            curdir += 1
            if curdir > 3:
                curdir = 0
        else:
            curdir -= 1
            if curdir < 0:
                curdir = 3

print(time)

"""
접근법: 
==============================================================================
개선점: 개선할 수 있는 부분
"""