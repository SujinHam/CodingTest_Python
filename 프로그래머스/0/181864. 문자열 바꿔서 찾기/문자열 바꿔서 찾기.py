def solution(myString, pat):
    ans = ""
    for elem in myString:
        if elem == "A":
            ans+="B"
        elif elem == "B":
            ans+="A"
    if pat in ans:
        return 1
    else:
        return 0