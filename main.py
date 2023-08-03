menu = {
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


def sufficient(order_ingredients):
    """return true when order can make, false when order cannot"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough


def coin():
    """Return total cost"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def go_through(received, drink_cost):
    """return True when payment is accepted"""
    if received >= drink_cost:
        change = round(received - drink_cost, 2)
        print(f"Here is your {change} change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refund")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink {drink_name}")


profit = 0
is_continue = True
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink = menu[choice]
        if sufficient(drink["ingredients"]):
            payment = coin()
            if go_through(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])
