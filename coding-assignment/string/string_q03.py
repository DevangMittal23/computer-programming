#Count Vowels in a String
string = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print(count)
