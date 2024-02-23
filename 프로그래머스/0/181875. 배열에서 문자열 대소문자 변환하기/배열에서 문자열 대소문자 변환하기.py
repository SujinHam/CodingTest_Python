def solution(strArr):
    answer = []
    
    for i, elem in enumerate(strArr):
        if i%2==1:
            answer.append(elem.upper())
        else:
            answer.append(elem.lower())
    return answer