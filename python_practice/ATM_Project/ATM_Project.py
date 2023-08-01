import time
import sys


CORRECT_PIN = 9618
BALANCE_AMOUNT = 100
SESSION_TIME = 100
VALID_TRANSACTIONS = 3

class InvalidPinException:
    pass


class InvalidBalanceException(Exception):
    def __init__(self, msg):
        self.msg = msg

class InvalidPinException(Exception):
    def __init__(self, msg):
        self.msg = msg

class InvalidAmountException(Exception):
    def __init__(self, msg):
        self.msg = msg

print(f"Please enter Your ATM card ")
time.sleep(2)
print(f"Your card has been detected, please proceed for transaction")

entered_pin_number= int(input("Please enter your ATM card pin: "))
try:
    if entered_pin_number == CORRECT_PIN:
        transaction = 0
        starting_time = time.time()
        print(f"Your card PIN is correct, Proceed with the transaction")
        print(f"Session starting_time: {starting_time}")
        entered_transaction_type = input(r"Please Enter D for deposit and  W for withdraw and L for Leave: ")
        while transaction<4 or time.time()-starting_time<100:
            if entered_transaction_type == "D":
                deposit_amount = int(input(r"Please enter Deposit amount: "))
                if deposit_amount ==0:
                    raise InvalidAmountException
                BALANCE_AMOUNT = BALANCE_AMOUNT+deposit_amount
                print(f"BALANCE_AMOUNT after Deposit: {BALANCE_AMOUNT}")
                transaction = transaction+1
            elif entered_transaction_type == "W":
                withdraw_amount = int(input(r"Please enter withdraw amount: "))
                if withdraw_amount ==0:
                    raise InvalidAmountException
                if withdraw_amount>BALANCE_AMOUNT:
                    raise InvalidBalanceException
                BALANCE_AMOUNT = BALANCE_AMOUNT-withdraw_amount
                print(f"BALANCE_AMOUNT after withdraw: {BALANCE_AMOUNT}")
                transaction = transaction + 1
            elif entered_transaction_type == "L":
                print(f"Leave transaction, closing the session")
    else:
        raise InvalidPinException
except InvalidPinException:
    raise InvalidPinException(msg="Your card PIN is correct")
except InvalidAmountException:
    raise InvalidAmountException(msg="Your card PIN is correct")
except InvalidBalanceException:
    raise InvalidBalanceException(msg="Your card PIN is correct")
except Exception as error:
    print(f"error is {error}")
finally:
    print(f"Plese collect your card, Please visit us again!!!")