def solution(my_string, n):
    answer = ''
    Len = len(my_string)
    for i in range(Len-n, Len):
        answer+=my_string[i]
        
    return answer