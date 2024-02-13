def solution(num_list):
    even = num_list[::2]
    odd = num_list[1::2]
    return max(sum(even), sum(odd))