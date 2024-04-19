def solution(park, routes):
    h = len(park)
    w = len(park[0]) #주어지는 원소의 길이는 무조건 3이기에, w = 3을 해도 무방할 것 같다. 
    x, y = 0, 0
    
    nav = {'S' : [1, 0], 'N' : [-1, 0], 'W' : [0, -1], 'E' : [0, 1]} #딕셔너리를 사용한다. 
    
    #시작점 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x = i
                y = j
                
    #route를 토대로 움직이기 시작
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        flag = 0
        step_x = x
        step_y = y
        for i in range(1, distance+1):
            step_x += nav[direction][0]
            step_y += nav[direction][1]
            if step_x>=h or step_x<=-1 or step_y>=w or step_y<=-1 or park[step_x][step_y]=='X':
                flag = 1
                break
        if flag == 0 :
            x += nav[direction][0]*distance
            y += nav[direction][1]*distance
    answer = [x, y]
    return answer