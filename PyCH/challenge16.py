# Function to return the first letter of the word
def first(word):
    return word[0]  # Return the first character of the string

# Function to return the last letter of the word
def last(word):
    return word[-1]  # Return the last character of the string

# Function to return the middle part of the word
def middle(word):
    return word[1:-1]  # Return the string excluding the first and last characters

# Function to check if a word is a palindrome
def is_palindrome(word):
    # Base case: If the word is empty or has one letter, it is a palindrome
    if len(word) <= 1:
        return True  # A word with length 1 or 0 is always a palindrome
    
    # Recursive case: check if the first and last letters are the same
    # and the middle part of the word is also a palindrome
    if first(word) == last(word):  # If the first and last letters match
        return is_palindrome(middle(word))  # Recursively check the middle part
    else:
        return False  # If the first and last letters don't match, it's not a palindrome

# Test cases
print(is_palindrome("noon"))  # Expected: True, "noon" is a palindrome
print(is_palindrome("redivider"))  # Expected: True, "redivider" is a palindrome
print(is_palindrome("hello"))  # Expected: False, "hello" is not a palindrome
print(is_palindrome("a"))  # Expected: True, A single character word is a palindrome
print(is_palindrome(""))  # Expected: True, An empty string is considered a palindrome
