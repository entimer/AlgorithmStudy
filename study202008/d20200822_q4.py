"""
작성일: 2020-08-22
==============================================================================
문제 위치: 교재 149p
==============================================================================
소요 시간: 18분
"""

# 입력
n, m = map(int, input().split())
ice_box = []
for i in range(n):
    ice_box.append(list(map(int, input())))

filled_ice_box = ice_box

# DFS 함수
def depth_first_search(row, col):
    if (row < 0) or (row >= n) or (col < 0) or (col >= m):
        return False
    
    if filled_ice_box[row][col] == 0:
        filled_ice_box[row][col] = 1

        depth_first_search(row + 1, col)
        depth_first_search(row - 1, col)
        depth_first_search(row, col + 1)
        depth_first_search(row, col - 1)
        return True
    else:
        return False

icecream_count = 0
for row in range(n):
    for col in range(m):
        if depth_first_search(row, col):
            icecream_count += 1

print(icecream_count)

"""
접근법: 한번 0인 부분을 찾았을 때 상하좌우로 연결된 모든 0인 부분을 찾아서 1로 바꾸고,
icecream count를 1 올리면 한 칸에 1개의 아이스크림이 생긴다는 것을 계산할 수 있다.

따라서, 2차원 행렬(얼음틀)의 처음부터 끝까지 탐색하면서 해당 좌표에 dfs를 돌리면 된다.
==============================================================================
개선점: filled_ice_box 리스트를 따로 만들 이유가 없다. 삭제하고 ice_box 리스트 하나만 쓰는것이 좋다.
==============================================================================
코멘트: 스터디 조원들의 코멘트
"""