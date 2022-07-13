MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Evaluate the remaining resources
def resource_eval(remain, order):
    """check if the machine has enough resources"""
    global MENU
    for ingredient in MENU[order]['ingredients']:
        if remain[ingredient] < MENU[order]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


# Make coffee
def make_coffee(remain, order):
    """use remaining resources to make coffee"""
    global MENU
    for ingredient in MENU[order]['ingredients']:
        remain[ingredient] -= MENU[order]['ingredients'][ingredient]
    return remain


# Evaluate the cost and process coins
def coin_machine(item):
    """takes customer's order and process coins"""
    global MENU
    cost = MENU[item]['cost']
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    coins_received = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    change = round(coins_received - cost, 2)
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here's ${change:.2f} in change.")
        print(f"Here's your {item} ☕️. Enjoy!")
    return cost


# Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
coffee_making = True
income = 0
while coffee_making:
    user_order = input("What would you like? (espresso/latte/cappuccino): ")

    # When entering "report" to the prompt, the user gets a report of the current remaining resources
    if user_order == 'report':
        for resource in resources:
            if resource == 'coffee':
                print(f"{resource.title()}: {resources[resource]}g")
            else:
                print(f"{resource.title()}: {resources[resource]}ml")
        print(f"Money: ${income:.2f}")

    # Turn off the coffee machine when user type "off" to the prompt
    elif user_order == 'off':
        coffee_making = False
    else:
        if resource_eval(resources, user_order):
            resources = make_coffee(resources, user_order)
            income += coin_machine(user_order)
