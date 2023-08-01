principle=2000
time=3
percentage=20
interest=(principle*time*percentage)/100
amount=principle+interest
print(f"interest is {interest} and amount is {amount}")


#####

def caliculate_interest_amount(principle,time,rate):
    interest=(principle*time*rate)/100
    amount=principle+interest
    return interest,amount

principle=float(input("enter principle amount") )
time=int(input("enter number of years"))
rate=float(input("enter rate of interest"))
amount,interest=caliculate_interest_amount(principle,time,rate)
print(f"amount is {amount}and interest is {interest}")


