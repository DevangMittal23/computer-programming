#Function to Check Palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))
print(is_palindrome("hello"))