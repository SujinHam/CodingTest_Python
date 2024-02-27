def solution(myString):
    return sorted([elem for elem in myString.split("x") if elem != ""])