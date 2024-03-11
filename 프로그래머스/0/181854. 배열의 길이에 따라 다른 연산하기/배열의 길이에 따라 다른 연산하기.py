def solution(arr, n):
    if len(arr)%2==1:
        for i in range(len(arr)//2+1):
            arr[2*i]+=n
    else:
        for i in range(len(arr)//2):
            arr[2*i+1]+=n
            
    return arr