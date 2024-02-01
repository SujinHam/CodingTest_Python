def solution(my_string):
    answer = []
    arr = [0 for _ in range(52)]
    for elem in my_string:
        if elem.isupper(): 
            k = 65
        else:
            k = 71
        arr[ord(elem)-k] += 1
    return arr