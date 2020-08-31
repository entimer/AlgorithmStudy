"""
작성일: 2020-08-31
==============================================================================
문제 위치: 교재 262p
==============================================================================
소요 시간: 못품
"""
import heapq

infinity = 100_000_000_000

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [infinity] * (n + 1)
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])

def find(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
        
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,  i[0]))

find(c)

count = 0
max_distance = 0

for d in distance:
    if d != infinity:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)

"""
접근법: 해결하지 못해 책의 소스를 보고 씀
==============================================================================
개선점: 다익스트라 알고리즘을 써야 한다는 것 까진 생각했지만 실제 구현에서 다양한 문제로 인해 오류를 겪음
다익스트라 구현을 좀더 공부해보는 것이 좋을 듯 함.
"""