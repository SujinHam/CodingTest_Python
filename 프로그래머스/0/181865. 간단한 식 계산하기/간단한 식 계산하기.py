def solution(binomial):
    binomial = binomial.split()
    a = int(binomial[0])
    b = int(binomial[2])
    if binomial[1]=="+":
        return a+b
    elif binomial[1]=="-":
        return a-b
    elif binomial[1]=="*":
        return a*b