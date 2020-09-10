# https://programmers.co.kr/learn/courses/30/lessons/60057
# 1시간 27분
def solution(s):
    answer = 0
    
    minimum = 10000
    for size in range(1, (len(s) // 2) + 2):
        cutted = [s[i * size:(i + 1) * size] for i in range((len(s) + size - 1) // size)]
        ziped = [0, cutted[0]]
        for cut in cutted:
            if ziped[-1] == cut:
                ziped[-2] += 1
            else:
                ziped.append(1)
                ziped.append(cut)
                
        count = 0
        for item in ziped:
            if item == 1:
                continue
            count += len(str(item))
        if minimum > count:
            minimum = count
    return minimum