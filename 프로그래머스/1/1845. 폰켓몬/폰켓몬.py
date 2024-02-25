def solution(nums):
    ans = len(set(nums))
    choose = len(nums)/2
    if ans<choose:
        return ans
    return choose