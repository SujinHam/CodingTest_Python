def solution(my_string):
    answer = []
    ch = ''
    Len = len(my_string)
    for i in range(Len, 0, -1):
        ch += my_string[i-1]
        rch = ch[::-1]
        answer.append(rch)
    answer.sort()
    return answer