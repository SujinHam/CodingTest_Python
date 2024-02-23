def solution(arr):
    answer = 0
    while True:
        change = []
        for elem in arr:
            if elem>=50 and elem%2==0:
                change.append(elem/2)
            elif elem<50 and elem%2==1:
                change.append(elem*2+1)
            else:
                change.append(elem) 
        if arr == change:
            return answer
        else:
            answer+=1
            arr=change