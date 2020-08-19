"""
작성일: 2020-08-19
==============================================================================
문제 위치: 교재 96p
==============================================================================
소요 시간: 17분
"""

# n과 m을 입력
n, m = map(int, input("").split())

# 입력받은 2차원 배열을 저장할 리스트
array = []

# 2차원 배열 입력
for i in range(n):
    # 라인별로 입력값을 리스트로 만들어 array에 추가
    input_list = list(map(int, input("").split()))
    array.append(input_list)

# 결과가 될 변수
# 결과값은 각 행의 카드 중 가장 작은 숫자들 중에서 가장 큰 값을 가져야 하므로 기본값을 가장 작은 0으로 결정
result = 0
for row in array:
    # min 함수를 이용해 각 행의 가장 작은 숫자를 얻음
    min_of_row = min(row)

    # result와 비교해서 result가 더 큰값으로 유지되도록
    if min_of_row > result:
        result = min_of_row

# 결과 출력
print(result)

"""
접근법: 이 문제의 해결법은 크게 구분해 2개의 단계로 진행된다.
1. 각 행의 최소값을 구한다.
2. 각 행의 최소값 중에서 최대값을 구한다.
따라서 매 행마다 가장 작은 수를 구하고 그 값이 가장 큰 수인지 확인하면 된다.
==============================================================================
개선점: 
- 아예 행마다 입력을 받을 때 최솟값을 구하고 대소를 비교했다면 반복문을 줄일 수 있고 array라는 변수도 만들 필요가 없다.
==============================================================================
코멘트: 스터디 조원들의 코멘트
"""