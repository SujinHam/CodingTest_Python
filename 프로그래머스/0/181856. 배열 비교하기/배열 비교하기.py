def solution(arr1, arr2):
        len1=len(arr1)
        len2=len(arr2)
        sum1=sum(arr1)
        sum2=sum(arr2)
        if len1!=len2:
            if len1>len2:
                return 1
            elif len2>len1:
                return -1
            else:
                return 0
        else:
            if sum1>sum2:
                return 1
            elif sum2>sum1:
                return -1
            else:
                return 0