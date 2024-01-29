def solution(my_string, is_prefix):
    ans = [my_string[:i] for i in range(len(my_string))]
    return 1 if is_prefix in ans else 0