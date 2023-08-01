"""
Author Raviteja
problem statement:
Condition with multiple functions
"""

def caliculate_interest_amount(principle,time,rate):
    interest=(principle*time*rate)/100
    amount=principle+interest
    return interest,amount
def caliculate_compound_interest_compound_amount(principle,time,rate):
    interest=(principle*(1+rate/100)**time-principle)
    amount=principle+interest
    return interest, amount

principle=float(input("Enter principle amount") )
time=int(input("Enter number of years"))
rate=float(input("Enter rate of interest"))
interest_type=input("Enter 's' if simple, enter 'c' if compound")
if interest_type == 's':
    amount,interest = caliculate_interest_amount(principle,time,rate)
elif interest_type == 'c':
    amount,interest=caliculate_compound_interest_compound_amount(principle,time,rate)
else:
    print("invalid input")
print(f"amount is {amount} and interest is {interest}")


