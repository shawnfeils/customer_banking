"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

    new_account = Account(float(balance),0)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    """ Assuming interest is accrued and compounded monthly. The exercise implies
    straight line non-compounding interest, however that would not fit the legal
    definition of a savings account in the U.S.
    """

    interest_earned = ((new_account.balance * ((1+((interest_rate/100)/12))**months)) - new_account.balance)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    updated_balance = (new_account.balance + interest_earned)

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    new_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    new_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    # print(new_account.balance)
    # print(interest_earned)
    # print(updated_balance)
    return new_account.balance, new_account.interest
           

# testing!
# if __name__ == "__main__":
#     create_savings_account(155,3.5,15)
    