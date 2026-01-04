# Day7_SimpleSimulation
# Task: Simulate a simple savings process:
#   - Ask for initial balance,
#   - monthly deposit,
#   - number of months.
# Each month:
#   - add deposit,
#   - print the balance.
# At the end, print total balance.
# Use a loop and clear formatting.
# Day7_SimpleSimulation

def simulate_savings():
    """Simulate a simple savings account over time"""
    print("=== Savings Account Simulation ===")
    
    try:
        # Get user inputs
        initial_balance = float(input("Enter initial balance: $"))
        monthly_deposit = float(input("Enter monthly deposit: $"))
        num_months = int(input("Enter number of months: "))
        
        # Validate inputs
        if num_months <= 0:
            print("Number of months must be positive.")
            return
        
        # Initialize variables
        current_balance = initial_balance
        total_deposited = 0
        
        print(f"\nStarting balance: ${initial_balance:.2f}")
        print("-" * 30)
        
        # Monthly simulation loop
        for month in range(1, num_months + 1):
            # Make deposit
            current_balance += monthly_deposit
            total_deposited += monthly_deposit
            
            # Print monthly statement
            print(f"Month {month}:")
            print(f"  Deposit: ${monthly_deposit:.2f}")
            print(f"  Balance: ${current_balance:.2f}")
            print("-" * 20)
        
        # Print final summary
        print("\n=== Simulation Complete ===")
        print(f"Total months simulated: {num_months}")
        print(f"Total deposited: ${total_deposited:.2f}")
        print(f"Final balance: ${current_balance:.2f}")
        print(f"Total growth: ${(current_balance - initial_balance):.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    simulate_savings()

if __name__ == "__main__":
    main()