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

total_machine_money = 0
total_client_money = 0
client_refund = 0
game_on = True
answer_right = False
out_of = []

#Todo 3: Print Report and shouuld include The Value of resources Water: 100ml, Milk: 50ml, Coffee: 76g, Money: $2.5
def report(total_machine_money):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${total_machine_money}"


#Todo 4:  Check resources sufficient?
def is_sufficient(answer, MENU):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    out_of = []
    negative = False
    for ingredient in MENU[answer]["ingredients"]:
        if ingredient == "water" and MENU[answer]["ingredients"][ingredient] > water:
            out_of.append(ingredient)
        elif ingredient == "coffee" and MENU[answer]["ingredients"][ingredient] > coffee:
            out_of.append(ingredient)
        elif ingredient == "milk" and MENU[answer]["ingredients"][ingredient] > milk:
            out_of.append(ingredient)
    return out_of

#Todo 5: Process coins. Calculate the monetary value of the coins inserted.
# E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def coin_processing(quarters_amount, dimes_amount, nickels_amount, pennies_amount):
    total_quarters = quarters_amount * 0.25
    total_dimes = dimes_amount * 0.10
    total_nickels = nickels_amount * 0.05
    total_pennies = pennies_amount * 0.01
    total_money = total_quarters + total_dimes + total_nickels + total_pennies
    return total_money


#Todo 7: Make a coffee deduct resources. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
def resource_deduction(answer, total_client_money, MENU, resources):
    return_to_client = 0
    cost_of_coffee = 0
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if answer == "espresso" and total_client_money >= float(MENU[answer]["cost"]):
        return_to_client = total_client_money - float(MENU[answer]["cost"])
        water -= MENU[answer]["ingredients"]["water"]
        milk -= 0
        coffee -= MENU[answer]["ingredients"]["coffee"]
        cost_of_coffee = float(MENU[answer]["cost"])
    elif answer == "latte" and total_client_money >= float(MENU[answer]["cost"]):
        return_to_client = total_client_money - float(MENU[answer]["cost"])
        water -= MENU[answer]["ingredients"]["water"]
        milk -= MENU[answer]["ingredients"]["milk"]
        coffee -= MENU[answer]["ingredients"]["coffee"]
        cost_of_coffee = float(MENU[answer]["cost"])
    elif answer == "cappuccino" and total_client_money >= float(MENU[answer]["cost"]):
        return_to_client = total_client_money - float(MENU[answer]["cost"])
        water -= MENU[answer]["ingredients"]["water"]
        milk -= MENU[answer]["ingredients"]["milk"]
        coffee -= MENU[answer]["ingredients"]["coffee"]
        cost_of_coffee = float(MENU[answer]["cost"])
    elif total_client_money < float(MENU[answer]["cost"]):
        return False
    return return_to_client, cost_of_coffee, water, milk, coffee


#Todo 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):
while game_on:
    answer = input("What would you like? (espresso/latte/cappuccino)").lower()
    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        out_of = is_sufficient(answer, MENU)
        if len(out_of) == 0:
            answer_right = True
        else:
            for ingredient in out_of:
                print(f"Sorry there is not enough {ingredient}.")
    elif answer == "off":
        game_on = False
    elif answer == "report":
        print(report(total_machine_money))
    elif answer != "espresso" or answer != "latte" or answer != "cappuccino":
        print("We dont have that, Try again")
    while answer_right:
        # Todo 2: Turn off the Coffee Machine by entering “off” to the prompt.
        quarters_amount = int(input("how many quarters?: "))
        dimes_amount = int(input("how many dimes?: "))
        nickels_amount = int(input("how many nickels?: "))
        pennies_amount = int(input("how many pennies?: "))

        total_client_money = coin_processing(quarters_amount, dimes_amount, nickels_amount, pennies_amount)
        deduction_or_no_money = resource_deduction(answer, total_client_money, MENU, resources)

        if deduction_or_no_money:
            client_refund = deduction_or_no_money[0]
            if client_refund != 0:
                print(f"Here is ${client_refund} dollars in change.")
            total_machine_money += deduction_or_no_money[1]
            resources["water"] = deduction_or_no_money[2]
            resources["milk"] = deduction_or_no_money[3]
            resources["coffee"] = deduction_or_no_money[4]
            print(f"Here is your {answer} enjoy")
        else:
            print("Sorry that's not enough money. Money Refunded")
        answer_right = False






        #Todo 6: Check transaction successful? And add the money if not enough money print “Sorry that's not enough money. Money refunded.”
