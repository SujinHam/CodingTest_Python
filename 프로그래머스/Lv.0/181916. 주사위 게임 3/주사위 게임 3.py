def solution(a, b, c, d):
    answer = 0
    list = [a, b, c, d]
    dice_list = set(list)  #중복을 없앤 리스트
    if len(dice_list) == 1:
        answer = 1111*a
    elif len(dice_list) == 2: #2개 2개씩 같게 나왔을 때
        for elem in list:
            if list.count(elem)==3: #같은 원소가 3개
                p = elem
                q = [x for x in dice_list if x!=p][0]
                answer = (10*p+q)**2
            elif list.count(elem) == 2: #같은 원소가 2개
                p = elem
                q = [x for x in dice_list if x != p][0]
                answer = (p + q)*(abs(p-q))
    elif len(dice_list) == 3:
        for elem in list:
            if list.count(elem)==2:
                p = elem
                q = [x for x in dice_list if x!=p][0]
                r = [x for x in dice_list if x!=p][1]
                answer = q*r
    else: #가장 작은 숫자
        answer = min(list)
                    
                
    return answer