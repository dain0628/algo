def solution(numbers):
    sum_numbers = 0
    for item in numbers:
        sum_numbers = sum_numbers + item
    answer = sum_numbers / len(numbers)   
    return answer
