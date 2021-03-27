def tickets(people):
    if people[0] == 50 or people[0] == 100:
        return 'NO'
    quantity_twenty_five = 0
    quantity_fifty = 0
    for i in people:
        if i == 25:
            quantity_twenty_five += 1
        elif i == 50:
            if quantity_twenty_five == 0:
                return 'NO'
            quantity_twenty_five -= 1
            quantity_fifty += 1
        elif i == 100:
            if (quantity_twenty_five < 1) or\
                    (quantity_twenty_five == 1 and quantity_fifty < 1) or\
                    (quantity_fifty == 0 and quantity_twenty_five < 3):
                return 'NO'
            if quantity_twenty_five >= 1 and quantity_fifty >= 1:
                quantity_twenty_five -= 1
                quantity_fifty -= 1
            elif quantity_twenty_five >= 3:
                quantity_twenty_five -= 3
    return "YES"
