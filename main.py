# 100-days-of-python-day-14  Coffee Machine

import data

MENU = data.MENU
resources = data.resources

machine_on = True


def check_resources(product):
    global resources
    enough_water = resources['water'] > MENU[product]['ingredients']['water']
    enough_milk = resources['milk'] > MENU[product]['ingredients']['milk']
    enough_coffee = resources['coffee'] > MENU[product]['ingredients']['coffee']
    if enough_coffee and enough_water and enough_milk:
        return True
    elif enough_water is False:
        print("Not enough water, please refill")
    elif enough_milk is False:
        print("Not enough milk, please refill")
    elif enough_coffee is False:
        print("Not enough coffee, please refill")
    return False


def print_cost(product):
    print(f"{product} costs ${format(MENU[product]['cost'], '.2f')}, please insert coins:\n")


def take_money(product):
    print_cost(product)
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))

    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    print(f"You have entered ${format(total, '.2f')}")
    return total


def make_coffee(product):
    global resources
    resources['water'] -= MENU[product]['ingredients']['water']
    resources['milk'] -= MENU[product]['ingredients']['milk']
    resources['coffee'] -= MENU[product]['ingredients']['coffee']
    resources['money'] += MENU[product]['cost']


def make_purchase(product):
    if not check_resources(product):
        return

    payment = take_money(product)
    cost = MENU[product]['cost']
    if payment >= cost:
        make_coffee(product)
        change = payment - cost
        print(f"Here is your {product} and change of ${format(change, '.2f')}")
    else:
        print("Insufficient funds.")


def refill():
    global resources
    water = int(input("How much water would you like to add?"))
    milk = int(input("How much milk would you like to add?"))
    coffee = int(input("How much coffee would you like to add?"))
    resources['water'] += water
    resources['milk'] += milk
    resources['coffee'] += coffee
    print("Refill complete")


def make_report():
    report = f'''
       water: {resources["water"]}ml
       milk: {resources["milk"]}ml
       coffee: {resources["coffee"]}g
       money: ${resources["money"]}
       '''
    print(report)


while machine_on:
    command = input("What would you like to order? (espresso, latte, cappuccino)\n")
    if command == "report":
        make_report()
    elif command == "refill":
        refill()
        make_report()
    elif command == "off":
        machine_on = False
    elif command == ("latte" or "cappuccino" or "espresso"):
        make_purchase(command)
    else:
        print("Please choose a type of coffee or use the commands report/refill/off")

