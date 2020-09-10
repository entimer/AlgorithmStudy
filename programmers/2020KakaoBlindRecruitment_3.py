# https://programmers.co.kr/learn/courses/30/lessons/60059
# 1시간 30분 (미해결)
import copy

def solution(key, lock):
    big_lock = create_big_lock(lock)
    for d in range(4):
        key = turn(key)
        match(key, big_lock)
    return False

# 시계방향으로 90도 회전
def turn(array):
    size = len(array[0])
    new_array = [[0] * size for _ in range(size)]
    for row in range(size):
        for col in range(size):
            new_array[col][size - 1 - row] = array[row][col]
    return new_array

# 가로세로가 3배인 배열 생성
def create_big_lock(lock):
    size = len(lock)
    big_size = size * 3
    big = [[0] * big_size for _ in range(big_size)]
    row = 0
    col = 0
    for x in range(size, size * 2):
        col = 0
        for y in range(size, size * 2):
            big[x][y] = lock[row][col]
            col += 1
        row += 1
    return big

def get_small_lock(big):
    size = len(big) // 3
    lock = [[0] * size for _ in range(size)]
    row = 0
    col = 0
    for x in range(size, size * 2):
        col = 0
        for y in range(size, size * 2):
            lock[row][col] = big[x][y]
            col += 1
        row += 1
    return lock

def match(key, big):
    for row in range(len(big) - len(key) + 1):
        for col in range(len(big) - len(key) + 1):
            vr = copy.deepcopy(big)
            for x in range(len(key)):
                for y in range(len(key)):
                    vr[row][col] += key[x][y]
            temp = get_small_lock(vr)
            if check(temp):
                return True
    return False

def check(lock):
    for x in range(len(lock)):
        for y in range(len(lock)):
            if lock[x][y] != 1:
                return False
    return True