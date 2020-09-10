# https://programmers.co.kr/learn/courses/30/lessons/60060
# 57분
def solution(words, queries):
    result = []
    for query in queries:
        result.append(check(words, query))
    return result

# 검색 키워드가 문자들중 몇개나 가능한지 리턴
def check(words, query):
    len_query = len(query)
    count_match = 0
    for word in words:
        # 길이가 같은 키워드만 비교
        if len(word) == len_query:
            count_wild = query.count('?')
            if query.find('?') == 0:
                if word[count_wild:] == query[count_wild:]:
                    count_match += 1
            else:
                if word[:len_query - count_wild] == query[:len_query - count_wild]:
                    count_match += 1
    return count_match