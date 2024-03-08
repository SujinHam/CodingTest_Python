def solution(arr):
    n = 0
    L = len(arr)
    while L>1:
        L/=2
        n+=1
    return arr+[0]*(2**n-len(arr))