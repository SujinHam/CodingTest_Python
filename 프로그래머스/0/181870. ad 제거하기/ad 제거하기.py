def solution(strArr):
    answer = []
    for elem in strArr:
        if 'ad' not in elem:
            answer.append(elem)
    return answer