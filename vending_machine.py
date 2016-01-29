from decimal import *
getcontext().prec = 4

coins = [1.0, .50, .20, .10, .05, .02, .01]
def give_change(amount):
    change = []
    amount = Decimal(str(amount))
    for coin in coins:
        coin = Decimal(str(coin))
        while coin <= amount:
            amount -= coin
            change.append(float(coin))
    return change

give_change(.18)
