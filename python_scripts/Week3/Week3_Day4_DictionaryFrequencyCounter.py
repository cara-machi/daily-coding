# Day4_DictionaryFrequencyCounter
# Task: Ask the user to input a sentence.
# Build a dictionary that counts how many times each word appears.
# Print each word with its count.
# Example: "hello world hello" → hello: 2, world: 1

# Day4_DictionaryFrequencyCounter

user_input = input("Please enter a sentence: ")
words = user_input.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")