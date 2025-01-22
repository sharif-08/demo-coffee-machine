menu ={
    "latte":{
        "ingredient":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":150,
    },
    "espresso":{
        "ingredient":{
            "water":50,
            "coffee":18,
        },
        "cost":100,
    },
    "cappuccino":{
        "ingredient":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":200,
    }
}

profit = 0
resource = {
    "water":500,
    "milk":500,
    "coffee":500
 }
def check_resource(order_indrigent):
    for item in order_indrigent:
        if order_indrigent[item]>resource[item]:
            print(f"sorry there is not enough {item}")
            return False
        return True
def process_coins():
    print("please insert coins. ")
    total = 0
    coins_five = int(input("how many 5rs coins:" ))
    coins_ten =  int(input("how many 10rs coins: "))
    coins_twenty = int(input("how many 20rs coins: "))
    total = coins_five*5 + coins_ten*10 + coins_twenty*20
    return total
def is_payment_successful(money_recived,coffee_cost):
    if money_recived>=coffee_cost:
        global profit
        profit += coffee_cost
        change = money_recived-coffee_cost
        print(f"here is your rs {change} in change. ")
        return True
    else:
        print("sorry that's not enough money. money refunded. ")
        return False
def make_coffee(coffee_name,coffee_ingredient):
    for item in coffee_ingredient:
        resource[item] -= coffee_ingredient[item]
    print(f"here is your {coffee_name}")
        
is_on=True
while is_on:
    choice = input("what would like to have ? (latte/espresso/cappuccino)\n")
    if choice == "off":
        is_on = False
    elif choice =="report":
        print(f"water = {resource['water']} ml")
        print(f"milk = {resource['milk']} ml")
        print(f"coffee = {resource['coffee']}")
        print(f"money = rs {profit}")
    else:
        coffee_type = menu[choice]
        print(coffee_type)
        if check_resource(coffee_type['ingredient']):
            payment = process_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredient'])