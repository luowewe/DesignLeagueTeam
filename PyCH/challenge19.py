def has_no_e(word):
    """Returns True if the given word doesn’t contain the letter 'e'."""
    for letter in word:  # Iterate through each letter in the word
        if letter == 'e':  # Check if the letter is 'e'
            return False  # Return False if 'e' is found
    return True  # Return True if 'e' is not found in the word

# Load words from a file or list
def filter_words_without_e(word_list):
    """Filters words that do not contain the letter 'e' and calculates the percentage."""
    words_without_e = [word for word in word_list if has_no_e(word)]  # Create a list of words without 'e'
    
    total_words = len(word_list)  # Get the total number of words in the list
    count_without_e = len(words_without_e)  # Count the number of words without 'e'
    
    percentage = (count_without_e / total_words) * 100 if total_words > 0 else 0  # Calculate the percentage
    
    print("Words without 'e':", words_without_e)  # Print words without 'e'
    print(f"Percentage of words without 'e': {percentage:.2f}%")  # Print the percentage with two decimal places

# Example usage
word_list = ["apple", "banana", "grape", "kiwi", "mango", "fig", "plum"]  # Define a sample word list
filter_words_without_e(word_list)  # Call the function with the word list
