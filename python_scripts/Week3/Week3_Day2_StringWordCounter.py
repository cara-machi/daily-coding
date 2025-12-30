# Day2_StringWordCounter
# Task: Ask the user to input a sentence.
# Count and print:
#   - total number of characters (excluding spaces),
#   - total number of words,
#   - how many times each vowel appears.
# Use loops and conditionals.

sentence = input("Which sentence would you like to observe: ")
parts = sentence.split()
word_count = len(parts)
print(f"There are {word_count} words")

char_count = 0
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in sentence:
    if not char.isspace():
        char_count += 1  
    
    lower_char = char.lower()
    if lower_char in vowel_counts:
        vowel_counts[lower_char] += 1

print(f"Character count (excluding spaces): {char_count}")

print("Vowel counts:")
for vowel, count in vowel_counts.items():
    print(f"  {vowel}: {count}")  