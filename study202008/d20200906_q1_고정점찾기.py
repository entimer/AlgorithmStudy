"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 368p
==============================================================================
소요 시간: 23분
"""

import sys

input = sys.stdin.readline

n = int(input().strip())
array = list(map(int, input().strip().split()))

def search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

a = search(array, 0, 0, len(array) - 1)
b = search(array, array[-1], 0, len(array) - 1)

if a == None and b == None:
    print(-1)
elif a == None and b != None:
    print(b)
else:
    print(a)

"""
접근법: 
이진 탐색을 2번 돌려서 고정점을 찾는다.
각 탐색마다 array[mid]가 mid와 같은지 알아본다.
두번의 탐색 결과가 모두 None이면 -1을 출력하고
하나라도 None이 아니면 그 값을 출력한다.
==============================================================================
개선점: 개선할 수 있는 부분
"""