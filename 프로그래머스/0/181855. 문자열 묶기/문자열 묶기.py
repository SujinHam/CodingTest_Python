def solution(strArr):
    arr = [len(i) for i in strArr] # strArr 원소의 길이들이 저장됨. 
    tmp = []
    for elem in set(arr):
        tmp.append(arr.count(elem))
    return max(tmp)