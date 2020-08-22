"""
작성일: 2020-08-22
==============================================================================
문제 위치: 교재 118p
==============================================================================
소요 시간: 60분
"""

# 입력
n, m = map(int, input().split())

# 최초 위치, 방향 입력
pos_x, pos_y, facing = map(int, input().split())

game_map = []              # 게임 맵

# 게임 맵 입력
for i in range(n):
    game_map.append(list(map(int, input().split())))

user_map = [[0] * m for i in range(n)]   # 유저가 방문한 지역 표시
user_map[pos_y][pos_x] = 1 # 시작지점 표시

# 이동한 칸수(기본적으로 시작칸이 있으므로 기본값 1)
move_count = 1

# 왼쪽 방향으로 회전하는 함수
def turn():
    global facing
    next_facing = facing - 1
    if next_facing < 0:
        next_facing = 3
    facing = next_facing

# 앞쪽이 이동 가능한지 체크하는 함수
def check_forward():
    if facing == 0:
        return check_can_move_to(pos_x, pos_y - 1)
    elif facing == 1:
        return check_can_move_to(pos_x + 1, pos_y)
    elif facing == 2:
        return check_can_move_to(pos_x, pos_y + 1)
    elif facing == 3:
        return check_can_move_to(pos_x - 1, pos_y)
        

# 뒤쪽이 이동 가능한지 체크하는 함수
def check_backward():
    if facing == 0:
        return check_can_move_to(pos_x, pos_y + 1)
    elif facing == 1:
        return check_can_move_to(pos_x - 1, pos_y)
    elif facing == 2:
        return check_can_move_to(pos_x, pos_y - 1)
    elif facing == 3:
        return check_can_move_to(pos_x + 1, pos_y)

# 해당 좌표로 이동이 가능한지 체크하는 함수
def check_can_move_to(x, y):
    # 목표 좌표가 육지이고 가보지 않은 곳이라면 True 아니면 False
    if (game_map[y][x] == 0) and (user_map[y][x] == 0):
        return True
    return False

# 이동 함수. 이동 후 방문 칸 수 1 증가
def move():
    global pos_x, pos_y, move_count
    if facing == 0:
        pos_y -= 1
    elif facing == 1:
        pos_x += 1
    elif facing == 2:
        pos_y += 1
    elif facing == 3:
        pos_x -= 1
    user_map[pos_y][pos_x] = 1
    move_count += 1

# 뒤로 이동 함수
def back():
    global pos_x, pos_y
    if facing == 0:
        pos_y += 1
    elif facing == 1:
        pos_x -= 1
    elif facing == 2:
        pos_y -= 1
    elif facing == 3:
        pos_x += 1


turn_count = 0  # 회전 횟수 카운트

# 캐릭터 이동 시작
while(True):
    turn()
    turn_count += 1
    
    if check_forward():
        move()
        turn_count = 0
        continue
    
    if turn_count >= 4:
        if check_backward():
            back()
            turn_count = 0
            continue
        else:
            break

print(move_count)

"""
접근법: 먼저 회전, 체크, 이동, 뒤로가기 각 행동별로 함수를 정의했다.(메인 로직에서의 쉬운 이해를 위해)
위치, 방향값은 확실한 관리를 위해 전역변수로만 사용하였다.
그 후 메인 로직에서 정의된 함수를 사용.
==============================================================================
개선점: 
- facing 처리에서 매번 0~3을 비교하기보다 방향별 이동값(dx, dy)를 정의해 사용했으면 더 쉬웠을 것.
==============================================================================
코멘트: 스터디 조원들의 코멘트
"""