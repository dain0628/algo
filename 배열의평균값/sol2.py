def solution(numbers):
    answer = 0

    total = 0

    for number in numbers:
        total = total + number
        i = i + 1

    print(total,i)
    answer = total / i
    return answer