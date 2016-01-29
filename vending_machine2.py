from decimal import Decimal

coins = [1, .50, .20, .10, .05, .02, .01]

available_items = {
    'coke': .73,
    'biscuits': 1.15,
    'apple': .43
}


def give_change(amount):
    change = []
    amount = Decimal(str(amount))
    for coin in coins:
        coin = Decimal(str(coin))
        while coin <= amount:
            amount -= coin
            change.append(float(coin))
    return change

# def get_choice():
#     prompt = 'choose item: %s' % available_items
#     chosen_item = raw_input(prompt)
#     if chosen_item not in available_items:
#         print "that item isn't available"
#         return
#
#     amount = raw_input('enter amount in pounds:')
#     cost = available_items[chosen_item]
#     if amount < cost:
#         print 'not enough money'
#     else:
#         change_to_return = float(amount) - cost
#         coins = give_change(change_to_return)
#         print "here's your change: %s" % coins


def give_item_and_change(item, amount):
    if item not in available_items:
        return None, None, "that item isn't available"

    cost = available_items[item]
    amount_split = amount.split(" ")
    total_amount = 0
    for amt in amount_split:
        total_amount += float(amt)

    # if amount < cost:
    if total_amount < cost:
        return None, amount, 'not enough money'

    change_to_return = float(total_amount) - cost
    coins = give_change(change_to_return)
    return item, coins, "here's your change"

if __name__ == '__main__':
    while True:
        # get_choice()
        item = raw_input('choose item: %s' % available_items)
        amount = raw_input('enter amount in pounds:')
        print give_item_and_change(item, amount)
