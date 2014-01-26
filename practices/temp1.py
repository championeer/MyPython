def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
    new_balance = balance-payment
    owed_balance = add_monthly_interest(new_balance)
    return owed_balance
	
new_bill = make_payment(bill/2,bill)
x = make_payment(100,new_bill)

print bill

print "You still owe: %f" %x
