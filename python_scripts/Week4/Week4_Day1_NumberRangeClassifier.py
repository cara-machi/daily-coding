# Day1_NumberRangeClassifier
# Task: Ask the user for an integer.
# Print whether the number is:
#   - negative, zero, or positive
#   - less than 10, between 10 and 50, or greater than 50
# Use nested if / elif / else statements.

# Day1_NumberRangeClassifier

def classify_number():
    """Classify a number based on multiple criteria"""
    print("=== Number Range Classifier ===")
    
    try:
        # Get user input
        number = int(input("Enter an integer: "))
        
        print(f"\nAnalyzing number: {number}")
        print("-" * 30)
        
        # First classification: positive, negative, or zero
        print("1. Sign classification:")
        if number > 0:
            print("   The number is POSITIVE")
        elif number < 0:
            print("   The number is NEGATIVE")
        else:
            print("   The number is ZERO")
        
        # Second classification: range classification
        print("\n2. Range classification:")
        if number < 10:
            print("   The number is LESS THAN 10")
        elif 10 <= number <= 50:
            print("   The number is BETWEEN 10 AND 50 (inclusive)")
        else:
            print("   The number is GREATER THAN 50")
        
        # Combined classification (optional, shows nested if/else)
        print("\n3. Combined classification:")
        if number < 0:
            print("   Negative and less than 10")
        elif number == 0:
            print("   Zero")
        elif number > 0:
            if number < 10:
                print("   Positive and less than 10")
            elif number <= 50:
                print("   Positive and between 10 and 50")
            else:
                print("   Positive and greater than 50")
        
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    classify_number()

if __name__ == "__main__":
    main()