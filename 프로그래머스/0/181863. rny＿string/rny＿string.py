def solution(rny_string):
    arr=""
    for elem in rny_string:
        if elem == "m":
            arr+="rn"
        else:
            arr+=elem
    return arr