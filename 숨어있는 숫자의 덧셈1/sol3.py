def solution(my_string):
    answer = 0
    numbers = []

    for char in my_string:
        if char in numbers:
            answer += int(char)

    return answer

    print(solution())