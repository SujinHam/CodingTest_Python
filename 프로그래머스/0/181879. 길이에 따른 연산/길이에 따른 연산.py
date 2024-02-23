def solution(num_list):
    start = 1
    if len(num_list)>=11:
        return sum(num_list)
    elif len(num_list)<=10:
        for num in num_list:
            start*=num
        return start