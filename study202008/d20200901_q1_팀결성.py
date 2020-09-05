"""
작성일: 2020-09-01
==============================================================================
문제 위치: 교재 298p
==============================================================================
소요 시간: 00분
"""

n, m = map(int, input().split())
array = [0] * (n + 1)
for i in range(0, n + 1):
    array[i] = i

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(array, a, b)
    elif o == 1:
        if find(array, a) == find(array, b):
            print("YES")
        else:
            print("NO")


"""
접근법: 내가 왜 이런 방식으로 문제를 해결했는지 작성
==============================================================================
개선점: 개선할 수 있는 부분
"""