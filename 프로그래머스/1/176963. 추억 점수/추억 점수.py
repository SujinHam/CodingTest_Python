def solution(name, yearning, photo):
    answer = []
    name_table = dict(zip(name,yearning))
    
    for people in photo:
        totalscore = 0
        for person in people:
            totalscore += name_table.get(person, 0)
        
        answer.append(totalscore)
    return answer