"""
작성일: 2020-08-25
==============================================================================
문제 위치: 교재 182p
==============================================================================
소요 시간: 7분
"""

n, k = map(int, input().split())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

array1.sort()
array2.sort(reverse=True)

for i in range(k):
    if array1[i] >= array2[i]:
        break
    array1[i], array2[i] = array2[i], array1[i]

print(sum(array1))
    

"""
접근법: 두 배열을 비교해서 array1로 큰 수를 몰아넣으면 된다.
먼저 비교의 용이성을 위해 두 배열을 모두 소팅하는데 array2의 경우 큰 값을 찾기 위해 내림차순으로 소팅한다.
다음 0번 인덱스부터 순서대로 비교해 큰 수를 array1로 몰아넣는다.
여기서 array2의 숫자가 같거나 커지는 순간 반복문을 종료한다.
그 후 array1의 숫자의 합을 출력한다.
==============================================================================
개선점: 개선할 수 있는 부분
==============================================================================
코멘트: 스터디 조원들의 코멘트
"""