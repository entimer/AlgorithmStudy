"""
작성일: 2020-08-26
==============================================================================
문제 위치: 교재 197p
==============================================================================
소요 시간: 9분
"""

n = int(input())
storage = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

storage.sort()

def search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid

    elif array[mid] < target:
        return search(array, target, mid + 1, end)

    else:
        return search(array, target, start, mid - 1)

for item in request:
    if search(storage, item, 0, n - 1):
        print("yes")
    else:
        print("no")


"""
접근법: 첫번째로 입력받은 배열에서 두번재로 입력받은 배열의 원소들이 있는지를 찾는 문제이다.
나의 경우 연습을 위해 굳이 이진 탐색을 사용해 보았다.
먼저 storage 리스트(가게의 부품)을 sort()로 정렬하였다. 그래야 이진 탐색이 가능하기 때문이다.
그리고 이진 탐색 함수를 만든 뒤,
request 리스트(손님의 요청)의 원소를 하나씩 꺼내 이진 탐색을 돌렸다.
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
코멘트: 이진 탐색에서 재귀 함수 형태를 사용할 때, 
return search(array, target, mid + 1, end)
또는
return search(array, target, start, mid - 1)
처럼 mid값에 1을 조정해주지 않으면 무한루프를 돈다. 참고하면 좋을듯.
"""