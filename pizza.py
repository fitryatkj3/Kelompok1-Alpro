#Class of 2024D
#Group Name {Fitrya Chalifatus Z(24091397117) and Fikro Nabila (24091397110)}
#import datetime is used to add a datetime module that functions to manipulate dates and times.
import datetime
#The code below is used to display a welcome greeting, enter a name, and greet the customer.
welcome = print(f"{"*" * 38}\n{"==== WELCOME TO D'PIZZA NYELL ====":^38}\n{"*" * 38}")
client_name = input("What's your name?")
print(f"Hallo {client_name}! Please input your order:")
#The code below is used to display the size options and select the desired size.
price = 0;
while True:
    size = input(f"{"Size Pizza:"}\n{"S = Small":<10} {"[10000]":>23}\n{"M = Medium":<10}{"[15000]":>24}\n{"L = Large":<10}{"[20000]":>24}\nChoose Size: ").upper()
    if size == "S":
        price += 10000
        fix = print(f"{"Small Size":<32}[{price}]")
        size_name = f"{"Small Size":<30}{10000}"
        break
    elif size == "M":
        price += 15000
        fix = print(f"{"Medium Size":<32}[{price}]")
        size_name = f"{"Medium Size":<30}{15000}"
        break
    elif size == "L":
        price += 20000
        fix = print(f"{"Large Size":<32}[{price}]")
        size_name = f"{"Large Size":<30}{20000}"
        break
    else:
        print("Invalid order. Repeat your order, please!")
#The code below is used to display the pizza crust options and select the desired crust variant.
while True:
    print(f"{"Crust Type:"}\n{"1 = Pan Pizza":<10} {"[20000]":>20}\n{"2 = Crown Crust":<10}{"[25000]":>19}\n{"3 = Cheesy Bites":<10}{"[30000]":>18}")
    crust = int(input("Choose Crust: "))
    if crust == 1:
        price += 20000
        fix = print(f"{"Pan Pizza":<32}[{price}]")
        crust_name = f"{"Pan Pizza":<30}{20000}"
        break
    elif crust == 2:
        price += 25000
        fix = print(f"{"Crown Crust":<32}[{price}]")
        crust_name = f"{"Crown Crust":<30}{25000}"
        break
    elif crust == 3:
        price += 30000
        fix = print(f"{"Cheesy Bites":<32}[{price}]")
        crust_name = f"{"Cheesy Bites":<30}{30000}"
        break
    else:
        print("Invalid order. Repeat your order, please!")
#The code below is used to display the pizza topping options and select the desired topping variant. 
while True:
    topping = input(f"{"Variant Toppings:"}\n{"F = Frankfurter BBQ":<10} {"[28000]":>14}\n{"M = Meat Monsta":<10}{"[35000]":>19}\n{"S = Super Supreme":<10}{"[42000]":>17}\n{"P = Paperoni":<10}{"[49000]":>22}\n{"C = Super Supreme Chicken":<10}{"[56000]":>9}\nChoose Topping: ").upper()
    if topping == "F":
        price += 28000
        fix = print(f"{"Frankfurter BBQ":<32}[{price}]")
        topping_name = f"{"Frankfurter BBQ":<30}{28000}"
        break
    elif topping == "M":
        price += 35000
        fix = print(f"{"Meat Monsta":<32}[{price}]")
        topping_name = f"{"Meat Monsta":<30}{35000}"
        break
    elif topping == "S":
        price += 42000
        fix = print(f"{"Super Supreme":<32}[{price}]")
        topping_name = f"{"Super Supreme":<30}{42000}"
        break
    elif topping == "P":
        price += 49000
        fix = print(f"{"Paperoni":<32}[{price}]")
        topping_name = f"{"Paperoni":<30}{49000}"
        break
    elif topping == "C":
        price += 56000
        fix = print(f"{"Super Supreme Chicken":<32}[{price}]")
        topping_name = f"{"Super Supreme Chicken":<30}{56000}"
        break
    else:
        print("Invalid order. Repeat your order, please!")
#The code below is used to display a question to the customer whether or not to add extra cheese.
cheese = input("Extra Cheese?(yes/no): ")
if cheese.lower() == "yes":
    price += 13000
    fix = print(f"{"Extra Cheese":<32}[{price}]")
    cheese_name = f"{"Extra Cheese":<30}{13000}"
else:
    price += 0
    cheese_name = "No Extra Cheese"
#The code below is used to display the order quantity fill.
quantity = int(input("Quantitiy: "))
quantity_price = 0;
if quantity >= 1:
    quantity_price = price*quantity
    print(quantity)
else:
    print(quantity)
#The code below is used to display the question whether to add an order or not.
new_order = input("Add an orders?(yes/no): ").lower()
if new_order == "yes":
    price1 = 0;
    quantity_price1 = 0;
    while True:
        print("Please input your order:")
        size1 = input(f"{"Size Pizza:"}\n{"S = Small":<10} {"[10000]":>23}\n{"M = Medium":<10}{"[15000]":>24}\n{"L = Large":<10}{"[20000]":>24}\nChoose Size: ").upper()
        if size1 == "S":
            price1 += 10000
            fix1 = print(f"{"Small Size":<32}[{price1}]")
            size_name1 = f"{"Small Size":<30}{10000}"
            break
        elif size1 == "M":
            price1 += 15000
            fix1 = print(f"{"Medium Size":<32}[{price1}]")
            size_name1 = f"{"Medium Size":<30}{15000}"
            break
        elif size1 == "L":
            price1 += 20000
            fix1 = print(f"{"Large Size":<32}[{price1}]")
            size_name1 = f"{"Large Size":<30}{20000}"
            break
        else:   
            print("Invalid order. Repeat your order, please!")

    while True:
        print(f"{"Crust Type:"}\n{"1 = Pan Pizza":<10} {"[20000]":>20}\n{"2 = Crown Crust":<10}{"[25000]":>19}\n{"3 = Cheesy Bites":<10}{"[30000]":>18}")
        crust1 = int(input("Choose Crust: "))
        if crust1 == 1:
            price1 += 20000
            fix1 = print(f"{"Pan Pizza":<32}[{price1}]")
            crust_name1 = f"{"Pan Pizza":<30}{20000}"
            break
        elif crust1 == 2:
            price1 += 25000
            fix1 = print(f"{"Crown Crust":<32}[{price1}]")
            crust_name1 = f"{"Crown Crust":<30}{25000}"
            break
        elif crust1 == 3:
            price1 += 30000
            fix1 = print(f"{"Cheesy Bites":<32}[{price1}]")
            crust_name1 = f"{"Cheesy Bites":<30}{30000}"
            break
        else:
            print("Invalid order. Repeat your order, please!")

    while True:
        topping1 = input(f"{"Variant Toppings:"}\n{"F = Frankfurter BBQ":<10} {"[28000]":>14}\n{"M = Meat Monsta":<10}{"[35000]":>19}\n{"S = Super Supreme":<10}{"[42000]":>17}\n{"P = Paperoni":<10}{"[49000]":>22}\n{"C = Super Supreme Chicken":<10}{"[56000]":>9}\nChoose Topping: ").upper()
        if topping1 == "F":
            price1 += 28000
            fix1 = print(f"{"Frankfurter BBQ":<32}[{price1}]")
            topping_name1 = f"{"Frankfurter BBQ":<30}{28000}"
            break
        elif topping1 == "M":
            price1 += 35000
            fix1 = print(f"{"Meat Monsta":<32}[{price1}]")
            topping_name1 = f"{"Meat Monsta":<30}{35000}"
            break
        elif topping1 == "S":
            price1 += 42000
            fix1 = print(f"{"Super Supreme":<32}[{price1}]")
            topping_name1 = f"{"Super Supreme":<30}{42000}"
            break
        elif topping1 == "P":
            price1 += 49000
            fix1 = print(f"{"Paperoni":<32}[{price1}]")
            topping_name1 = f"{"Paperoni":<30}{49000}"
            break
        elif topping1 == "C":
            price1 += 56000
            fix1 = print(f"{"Super Supreme Chicken":<32}[{price1}]")
            topping_name1 = f"{"Super Supreme Chicken":<30}{56000}"
            break
        else:
            print("Invalid order. Repeat your order, please!")

    cheese1 = input("Extra Cheese?(yes/no): ")
    if cheese1.lower() == "yes":
        price1 += 13000
        fix1 = print(f"{"Extra Cheese":<32}[{price1}]")
        cheese_name1 = f"{"Extra Cheese":<30}{13000}"
    else:
        price1 += 0
        cheese_name1 = "No Extra Cheese"

    quantity1 = int(input("Quantitiy: "))
    quantity_price1 = 0;
    if quantity1 >= 1:
        quantity_price1 = price1*quantity1
        print(quantity1)
    else:
        print(quantity1)
else:
    quantity_price1 = 0
#The code below is used to display the question whether the order is dine-in or takeaway.
quantity_price2 = quantity_price+quantity_price1
dine_status = "";
price_status = 0;
dine_in = input("Dine in?(yes/no): ").lower()
if dine_in == "yes":
    price_status = quantity_price2 * (5 / 100)
    dine_status = "== Dine in =="
else:
    price_status = quantity_price2 * (10 / 100)
    dine_status = "== Take Away =="
#The code below is used to display the order number automatically.
def order_numb():
    order_count = 1
    order_number = f"ORDER-{order_count:04d}"
    order_count += 1
    return order_number

ordernumbdef = order_numb()
def bill_number():
    order_num = ordernumbdef
    print(f"Bill Number: {order_num}")
#The code below is used to display the order date and time automatically.
def prod_time():
    prod = datetime.datetime.now()
    print(f"Date: {prod}")

grandtotal = quantity_price2+price_status
#The code below is used to display the payment amount.
print(f"{"Sub-total":<32}{quantity_price2}\n{"Tax":<32}{price_status}\n{"Grand-total":<32}{grandtotal}")
#The code below is used to input payment and calculate change.
while True:
    cash = int(input("Money: "))
    change = 0;
    if cash >= grandtotal:
        change = cash-grandtotal
        break
    else:
        print("Not enough payments")
print(f"{"Change:":<31} {change}")
#The code below is used to enter the cashier's name.
cashier = input("Cashier name? ")

#The code below is used to display the order bill.
def bill():
    print(f"\n{"#" * 38}\n{"~~~~~~~~~~~ D'PIZZA NYELL ~~~~~~~~~~~":^38}\n{"#" * 38}\n ")
    print(f"{"Class of 2024D with NIM 117-110":^38}\n \n{"-" * 38}\n ")
    print(f"Name: {client_name}\n ")
    print(f"{dine_status:^38}\n{"-" * 38}\n ")
    bill_number()
    prod_time()
    print(f"Cashier: {cashier}\n{"-" * 38}")
    print(f"Pizza{quantity:^35}")
    print(f"{size_name}\n{crust_name}\n{topping_name}\n{cheese_name}")
    if new_order == "yes":
        print(f"Pizza{quantity1:^35}")
        print(f"{size_name1}\n{crust_name1}\n{topping_name1}\n{cheese_name1}")
    print(f" \n{"-" * 38}\n{"Sub-total":<30}{quantity_price2}")
    print(f"{"Tax":<30}{price_status}\n{"-"*8:>38}")
    print(f"{"GRAND TOTAL":<30}{grandtotal}")
    print(f"{"Cash":<30}{cash}\n{"-"*8:>38}")
    print(f"{"Change":<30}{change}")
    print(f"{"=" * 38}\n{"Closed Bill":^38}\n \n{"===== Thank you for your order =====":^38}\n{"Enjoy your meal!":^38}\n \n{"<-------- JANGAN HUTANG!!! -------->":^38}\n ")

bill()



