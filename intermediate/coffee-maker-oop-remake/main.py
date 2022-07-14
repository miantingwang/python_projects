from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()
items = menu.get_items()
coffee_making = True

while coffee_making:
    # prompt the user to choose their drink
    user_order = input(f"What would you like? ({items}): ")

    # when the user asks for the report
    if user_order == 'report':
        cm.report()
        mm.report()

    elif user_order == 'off':
        coffee_making = False
    # if the resources are sufficient to make the order,

    else:
        order = menu.find_drink(user_order)
        if cm.is_resource_sufficient(order):
            mm.make_payment(order.cost)
            cm.make_coffee(order)

