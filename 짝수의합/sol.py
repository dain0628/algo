def solution(n)
    answer = 0
    for item in range(1,n+1):
        if item % 2 == 0:
            answer = answer + item        
    return answer