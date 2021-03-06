"""
작성일: 2020-00-00
==============================================================================
문제 위치: 교재 178p
==============================================================================
소요 시간: 5분
"""

n = int(input())

array = []
for a in range(n):
    array.append(int(input()))

for i in range(len(array)):
    max_index = i
    for j in range(i + 1, len(array)):
        if array[max_index] < array[j]:
            max_index = j
    temp = array[i]
    array[i] = array[max_index]
    array[max_index] = temp

for i in array:
    print(i, end=' ')

"""
접근법: 간단하게 선택정렬로 배열 정렬.
==============================================================================
개선점: 파이썬의 기본 정렬 함수가 있다.
==============================================================================
코멘트: 스터디 조원들의 코멘트
"""