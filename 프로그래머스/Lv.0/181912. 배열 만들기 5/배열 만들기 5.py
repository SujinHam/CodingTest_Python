def solution(intStrs, k, s, l):
    answer = []
    for elem in intStrs:
        subString = ''.join(elem[s:s+l])
        subString = int(subString)
        if subString>k:
            answer.append(subString)
    
    return answer