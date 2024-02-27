def solution(myStr):
    myStr = myStr.replace("a"," ")
    myStr = myStr.replace("b"," ")
    myStr = myStr.replace("c"," ")
    myStr = myStr.split()
    if len(myStr)==0:
        return ["EMPTY"]
    return myStr