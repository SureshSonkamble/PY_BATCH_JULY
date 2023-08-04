def count_words(input_string):
    words = input_string.split()
    return len(words)

# Test the function
text = "This is a sample text with some words in it and we are counting"
word_count = count_words(text)
print("Word count:", word_count)
