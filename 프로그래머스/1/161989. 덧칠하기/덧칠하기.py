def solution(n, m, section):  # 그리디 알고리즘을 사용하는 문제
    cnt = 1 # 가장 먼저 칠해야 할 곳 포함. paint 1 부터 시작한다. 
    start = section[0] # 첫 번째 빈 구역부터 시작
    for i in range(1, len(section)):
        if section[i] - start >= m:
            cnt += 1
            start = section[i]  # 그 다음 빈 구역으로 start를 갱신
    return cnt