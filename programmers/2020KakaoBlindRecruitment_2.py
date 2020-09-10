# https://programmers.co.kr/learn/courses/30/lessons/60058
# 34분
def solution(p):
    if p == '' or p == None:
        return ''
    if check_correct(p):
        return p
    answer = change_string(p)
    return answer

def check_correct(p):
    stack = []
    for index in range(len(p)):
        item = p[index]
        if item == '(':
            stack.append(item)
        else:
            if len(stack) <= 0:
                return False
            else:
                stack.pop()
    return True

def change_string(p):
    # 1단계
    if p == '' or p == None:
        return ''
    # 2단계
    count_open = 0
    count_close = 0
    u = ''
    v = ''
    index = 0
    for i in range(len(p)):
        item = p[i]
        if item == '(':
            count_open += 1
            u += item
        else:
            count_close += 1
            u += item
        if count_open == count_close:
            index = i
            break
    v = p[index + 1:]
    # 3단계
    if check_correct(u):
        result = change_string(v)
        # 3-1단계
        return u + result
    # 4단계
    else:
        # 4-1단계
        new_string = '('
        # 4-2단계
        new_string += change_string(v)
        # 4-3단계
        new_string += ')'
        u = u[1:]
        u = u[:-1]
        u = reverse(u)
        new_string += u
        return new_string

def reverse(p):
    newstring = ''
    for i in range(len(p)):
        if p[i] == '(':
            newstring += ')'
        else:
            newstring += '('
    return newstring