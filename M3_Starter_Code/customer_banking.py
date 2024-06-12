# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("What is the initial savings balance? "))
    savings_interest = float(input("What is the APR for the savings account? "))
    savings_period = int(input("How many months will you keep the savings balance? "))

    # Call the create_savings_account function and pass the variables from the user.
    """ Savings accounts do not have a maturity; they are demand deposit accounts.
    """
    updated_savings_balance, sav_interest_earned = create_savings_account(savings_balance, savings_interest, savings_period)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print(f"Your savings account balance will be ${updated_savings_balance:,.2f} in {savings_period} months, including ${sav_interest_earned:,.2f} of earned interest")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    cd_balance = float(input("What is the initial CD balance? "))
    cd_interest = float(input("What is the APR for the CD? "))
    cd_maturity = int(input("What is the CD term to maturity (in months)? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print(f"Your CD balance will be ${updated_cd_balance:,.2f} in {cd_maturity} months, including ${cd_interest_earned:,.2f} of earned interest")

if __name__ == "__main__":
    # Call the main function.
    main()