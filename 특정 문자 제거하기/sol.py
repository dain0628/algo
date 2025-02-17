vowels = 'aeiou'

for char in vowels:
    words = words.replace(char, '')

print(words)

def solution(my_string, letter):
    answer = letter
    for letter in my_string:
        my_string.remove(letter)
    return answer