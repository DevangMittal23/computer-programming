#Count Occurrences of Characters in a String
def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(count_characters("hello world"))

