def solution(str_list):
    answer = []
    for elem in str_list:
        if elem == "l":
            return str_list[:str_list.index("l")]
        elif elem == "r":
            return str_list[str_list.index("r")+1:]
        else:
            answer = []
    return answer