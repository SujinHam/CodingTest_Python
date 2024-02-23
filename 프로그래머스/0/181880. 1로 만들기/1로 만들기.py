def solution(num_list):
    answer = 0
    for elem in num_list:
        while elem>1: 
            if elem%2==0:
                elem/=2
            else:
                elem = (elem-1)/2
            answer+=1
    
    return answer