# Day6_FileReadAndAnalyze
# Task: Read text from a file named 'data.txt'.
# Compute and print:
#   - number of lines,
#   - number of words,
#   - number of characters.
# You may assume the file exists in the same folder.
# Use open(), read(), and loops.

# Day6_FileReadAndAnalyze

def read_and_analyze_file(filename):
    """Read a file and analyze its contents"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Count lines
        lines = content.split('\n')
        num_lines = len(lines)
        
        # Count words
        words = content.split()
        num_words = len(words)
        
        # Count characters
        num_chars = len(content)
        
        # Print results
        print(f"File: {filename}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    # Read and analyze 'data.txt'
    read_and_analyze_file('data.txt')

if __name__ == "__main__":
    main()