def solution(myString, pat):
    cnt=0
    idx=0
    while True:
        mom = myString.find(pat,idx)
        if mom==-1:
            break
        cnt+=1
        idx=mom+1
    return cnt