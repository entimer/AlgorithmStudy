"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 152p
==============================================================================
소요 시간: 44분
"""

from collections import deque

# 입력
n, m = map(int, input().split())

# 미로 입력
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

# 이동방향(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 길찾기 함수
# x, y: 현재 좌표
# px, py: 이전 좌표
def find(x, y, px, py):
    if (x < 0) or (x >= n) or (y < 0) or (y >= m):
        return False
    
    if maze[x][y] == 1:
        maze[x][y] = maze[px][py] + 1
        find(x + 1, y, x, y)
        find(x - 1, y, x, y)
        find(x, y + 1, x, y)
        find(x, y - 1, x, y)
        return True
    else:
        return False

find(0, 0, 0, 0)
print(maze[n - 1][m - 1] - 1)

"""
접근법: 
1. 해당 좌표의 값이 1이면 한번도 가보지 않은 곳이다.
2. 좌표를 차례대로 방문하면서 (이전 좌표의 값 + 1)을 하면 시작점으로부터의 거리가 된다.

따라서, (0,0)부터 하나씩 탐색하며 1인 부분에 이전 좌표의 값을 더한다.
단, 시작점 역시 1이 추가되기 때문에 1을 빼야 정상적인 거리값이 된다.
==============================================================================
개선점: 재귀함수를 사용하지 않고도 풀수 있다. (큐를 사용하는 방법)
==============================================================================
코멘트: 스터디 조원들의 코멘트
"""