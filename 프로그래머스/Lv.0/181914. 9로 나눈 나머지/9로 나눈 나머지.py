def solution(number):
    answer = 0
    num = 0
    for elem in number:
        elem = int(elem)
        num += elem
        answer = num%9
    return answer