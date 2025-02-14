def solution(n,k)
answer = 0

        #양꼬치 총액    음료수 총액   서비스 음료 가격   
answer = (n * 12000) + (k * 2000) - (n//10 * 2000)