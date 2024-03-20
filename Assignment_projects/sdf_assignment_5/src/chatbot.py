"""
Description: Chatbot application. Allows user to perform
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456: {"balance": 1000.0},
    789012: {"balance": 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:


def get_account() -> int:
    """
    This function defines and collect user input
    for processing account information
    :exception: This function raise an exception if invalid account is entered
    :return: integer
    """
    try:
        prompt = int(input("Please enter your account number: "))
        if prompt not in ACCOUNTS:
            raise Exception('Account number entered does not exist.')
        else:
            return prompt
    except ValueError:
        raise ValueError("Account number must be a whole number.")


def get_amount() -> float:
    """
    This function returns an amount entered by the user
    if the input is parsed to integer and its > than 0
    :exception: raise an exception if invalid input is captured
    :return: float
    """
    try:
        prompt = float(input("Enter the transaction amount: "))
    except ValueError:
        raise ValueError("Invalid amount. Amount must be numeric.")

    if prompt <= 0:
        raise ValueError('Invalid amount. Please enter a positive number.')

    return prompt


def get_balance(account: int) -> str:
    """
    This function gets an input from a user which is an account number,
    it hence checks if the account number exist in the assumed database,
    if yes, the account balance is returned else an exception is raised.
    :exception: raise an exception if an invalid account number is inputted
    :return: str
    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    return f'Your current balance for account {account} is ${ACCOUNTS.get(account).get("balance"):,.2f}.'


def make_deposit(account: int, amount: float) -> str:
    """
        This function is defined for a user to make deposit to its
        associated account. The function raises an error when the account
        entered does not exist and as well raises an error if the input
        amount is negative.
        :exception: raise an exception if an invalid account number is inputted
        :return: str
    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    elif amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")
    else:
        initial_balance = ACCOUNTS.get(account)['balance']
        updated_balance = initial_balance + amount
        ACCOUNTS[account]['balance'] = updated_balance
        return f'You have made a deposit of ${amount:,.2f} to account {account}.'


def user_selection() -> str:
    """
    This function create 3 list items a user can select from;
    the list includes balance checking, depositing and exiting
    :return: It returns a corresponding value per user selection
    :exception: this is raised when an invalid selection is made
    """
    prompt = input("what will you like to do (balance/deposit/exit)? ")
    if prompt.lower() not in VALID_TASKS:
        raise Exception('Invalid task. Please choose balance, deposit, or exit.')
    return prompt.lower()

## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION


def chatbot():
    """
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    """

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:
            selection = user_selection()

            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:
                        account = get_account()
                        valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                    ## CALL THE get_balance FUNCTION HERE
                    ## PASSING THE account VARIABLE DEFINED
                    ## ABOVE, AND PRINT THE RESULTS:
                    print(get_balance(account))

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:
                            amount = get_amount()


                            valid_amount = True
                        except Exception as e:
                            # Invalid amount.
                            print(e)
                    ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                    ## VARIABLES account AND amount DEFINED ABOVE AND 
                    ## PRINT THE RESULTS:
                    print(make_deposit(account, amount))
            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")


if __name__ == "__main__":
    chatbot()
