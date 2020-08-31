"""
작성일: 2020-08-30
==============================================================================
문제 위치: 교재 259p
==============================================================================
소요 시간: 30분
"""
INFINITY = 100_000

n, m = map(int, input().split())

connect_list = [[INFINITY] * (n + 1) for _ in range(n + 1)]
for x in range(1, n +1):
    for y in range(1, n + 1):
        if x == y:
            connect_list[x][y] == 0

for _ in range(m):
    comp1, comp2 = map(int, input().split())
    connect_list[comp1][comp2] = 1
    connect_list[comp2][comp1] = 1

x, k = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for l in range(1, n + 1):
            connect_list[j][l] = min(connect_list[j][l], connect_list[j][i] + connect_list[i][l])

distance = connect_list[1][k] + connect_list[k][x]

if distance >= INFINITY:
    print(-1)
else:
    print(distance)

"""
접근법: 책에 있는 플로이드 워셜 알고리즘을 그대로 쓰다 보니 소스가 거의 같다.
==============================================================================
개선점: 반복문용 변수 i, j, l이 너무 비슷하게 생겨 오류 고치는데 시간을 많이 사용했다.
반복변수는 이렇게 쓰지 않는 것이 좋겠다.
"""