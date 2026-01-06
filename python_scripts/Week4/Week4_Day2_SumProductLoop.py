# Day2_SumProductLoop
# Task: Ask the user how many numbers they want to input (n).
# Use a loop to read n numbers.
# Compute and print:
#   - the sum,
#   - the product of all numbers.
# Use an accumulator for both sum and product.

def main():
    n=int(input("how many numbers u want to input"))
    number=[]
    for i in range(n):
        num=int(input(f"what is number {i+1} "))
        number.append(num)
    total=0
    product=1
    for num in number:
        total += num
        product *= num
    print (product,total)
main()

