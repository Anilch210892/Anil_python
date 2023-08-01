"""
Author Anilkumar
problem statement: caliculating simple interest
input: principle,time,rate
output: interest, amount
"""
def caliculate_interest_amount(principle,time,rate,interest_type):
    if interest_type == 's':
        interest=(principle*time*rate)/100
    elif interest_type == 'c':
        interest = (principle * (1 + rate / 100) ** time - principle)
    amount=principle+interest
    return amount,interest


principle = float(input("Enter principle amount") )
time=int(input("Enter number of years"))
rate=float(input("Enter rate of interest"))
interest_type=input("Enter 's' if simple, enter 'c' if compound")
amount,interest = caliculate_interest_amount(principle,time,rate,interest_type)

print(f"amount is {amount} and interest is {interest}")


