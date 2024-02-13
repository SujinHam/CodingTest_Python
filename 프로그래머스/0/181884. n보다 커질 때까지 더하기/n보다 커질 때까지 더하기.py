def solution(numbers, n):
    add = 0
    for elem in numbers:
        add += elem
        if add>n:
            return add