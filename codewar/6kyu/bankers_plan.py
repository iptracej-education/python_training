


# f0: total deposit 
# p: interest rate  
# c0 : withdrawal amount  
# i: inflation  

def fortune(f0, p, c0, n, i): 

    balances = {f0}
    balance = f0
    interest_rate = p
    expense = c0
    inflation = i
    
    for year in range(1, n):

        balance = balance - expense
        print(f"{balance} this is the balance at each year")
 
        # Check if the balance is 0 or less         
        if balance <= 0:
            return False
    
        balance = balance + (balance * (p/100))
        print(f"{balance} this is the interest-added balance at the end of the year")
        
        # expense = expense + (expense * (i/100))
        expense = int(expense * (1 + i / 100) + 0.9999)
        print(f"{expense} this is the interest-added balance at the end of the year")

    return balance > 0

print(fortune(100000, 1, 9185, 12, 1))
    
    
"""
def fortune_with_details(f0, p, c0, n, i):
    
    Determines if John can make a living for n years based on the initial deposit,
    interest rate, withdrawal amount, and inflation rate.
    Prints the balance at the beginning of each year and the result.
    
    balances = [f0]  # List to track balances at the beginning of each year
    balance = f0
    withdrawal = c0

    for year in range(1, n):
        # Add interest for the year
        interest = int(balance * (p / 100))
        balance += interest
        
        # Deduct living expenses for the year
        balance -= withdrawal
        
        # Add the balance for the next year
        balances.append(balance)
        
        # If balance becomes negative, John cannot sustain
        if balance < 0:
            print(f"Balances at the beginning of each year: {balances}")
            print(f"Result: False (John cannot sustain for {n} years)")
            return balances, False

        # Update withdrawal amount with inflation
        withdrawal = int(withdrawal * (1 + i / 100))

    print(f"Balances at the beginning of each year: {balances}")
    print(f"Result: True (John can sustain for {n} years)")
    return balances, True

# Test case
balances, result = fortune_with_details(100000, 1, 9185, 12, 1)

"""
