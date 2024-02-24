def solution(myString):
    ans = []
    arr = myString.split('x')
    for elem in arr:
        ans.append(len(elem))
    return ans