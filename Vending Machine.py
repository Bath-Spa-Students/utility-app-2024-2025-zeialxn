# welcome message
print("Welcome to The Filipino Snacks Vending Machine!")
print("Please take a look at our menu.")
print(" ")

# menu with item code, product name, stock, price, and category
menu = [
    {"item code": "A1", "product name": "Regent Golden Sweet Corn", "stock": 5, "price": 20, "category": "CHIPS"},
    {"item code": "A2", "product name": "Jack ‘n Jill Vcut Spicy BBQ Potato Chips", "stock": 5, "price": 20, "category": "CHIPS"},
    {"item code": "A3", "product name": "Moby Caramel Puffs", "stock": 5, "price": 20, "category": "CHIPS"},
    {"item code": "A4", "product name": "Oishi Ribbed Cracklings Salt & Vinegar", "stock": 5, "price": 20, "category": "CHIPS"},
    {"item code": "B1", "product name": "Choco Mucho Milk Chocolate Wafer Roll", "stock": 5, "price": 10, "category": "CHOCOLATE BARS"},
    {"item code": "B2", "product name": "Choco Mucho White Chocolate Caramel Wafer Roll", "stock": 5, "price": 10, "category": "CHOCOLATE BARS"},
    {"item code": "B3", "product name": "Jack ‘n Jill Cloud 9 Classic Chocolate Bar", "stock": 5, "price": 10, "category": "CHOCOLATE BARS"},
    {"item code": "B4", "product name": "Jack ‘n Jill Big Bang Classic Chocolate Bar", "stock": 5, "price": 10, "category": "CHOCOLATE BARS"},
    {"item code": "C1", "product name": "C2 Apple Green Tea", "stock": 5, "price": 15, "category": "DRINKS"},
    {"item code": "C2", "product name": "C2 Lemon Green Tea", "stock": 5, "price": 15, "category": "DRINKS"},
    {"item code": "C3", "product name": "C2 Classic Green Tea", "stock": 5, "price": 15, "category": "DRINKS"},
    {"item code": "C4", "product name": "Nature’s Spring Bottled Water", "stock": 5, "price": 13, "category": "DRINKS"},
]

# function to display the menu
def display_menu():
    print(": Item Code :                  Product Name                   : Stock : Price :")
    
    # chips category
    print("------------------------------------CHIPS--------------------------------------")
    chips_category = [
        ["A1", "Regent Golden Sweet Corn", 5, 20],
        ["A2", "Jack ‘n Jill Vcut Spicy BBQ Potato Chips", 5, 20],
        ["A3", "Moby Caramel Puffs", 5, 20],
        ["A4", "Oishi Ribbed Cracklings Salt & Vinegar", 5, 20]
    ]
    for item in chips_category:
        print(f": {item[0]:<9} : {item[1]:<47} : {item[2]:<5} : {item[3]:<5} :")
    
    # chocolate bars category
    print("-------------------------------CHOCOLATE BARS----------------------------------")
    chocolatebars_category = [
        ["B1", "Choco Mucho Milk Chocolate Wafer Roll", 5, 10],
        ["B2", "Choco Mucho White Chocolate Caramel Wafer Roll", 5, 10],
        ["B3", "Jack ‘n Jill Cloud 9 Classic Chocolate Bar", 5, 10],
        ["B4", "Jack ‘n Jill Big Bang Classic Chocolate Bar", 5, 10]
    ]
    for item in chocolatebars_category:
        print(f": {item[0]:<9} : {item[1]:<47} : {item[2]:<5} : {item[3]:<5} :")
    
    # drinks category
    print("-----------------------------------DRINKS--------------------------------------")
    drinks_category = [
        ["C1", "C2 Apple Green Tea", 5, 15],
        ["C2", "C2 Lemon Green Tea", 5, 15],
        ["C3", "C2 Classic Green Tea", 5, 15],
        ["C4", "Nature’s Spring Bottled Water", 5, 13]
    ]
    for item in drinks_category:
        print(f": {item[0]:<9} : {item[1]:<47} : {item[2]:<5} : {item[3]:<5} :")

# function to get product details by user input of item code
def input_item_code(code):
    for item in menu:
        if item["item code"] == code:
            return item
    return None

if __name__ == "__main__":
    while True:
        display_menu()
        user_input_code = ""

        # user input of item code
        while True:
            print("\nType a product code to continue...")
            user_input_code = input().upper()
            product = input_item_code(user_input_code)
            if product: #if there is no stock left, the user will be asked to choose another product
                if product["stock"] == 0:
                    print(f"Oops! {product['product name']} is out of stock.. Please select a different product.")
                else: #if there is still stocks left, it will print the product name, its price nad how many stocks left
                    print(f"You selected {product['product name']}. Please pay {product['price']} pesos.")
                    print(f"Stock available: {product['stock']}")
                    break
            else: #if the user enters an input that is not in the menu, it will print that it is invalid and will prompt to enter a valid code
                print("The code you input is invalid. Please enter a valid code.")

        # inserting of money
        money_inserted = 0
        while True:
            print(f"Inserted money: {money_inserted} pesos") # this shows how much the user have inserted already
            print("Insert your money here:") # this is where the user can enter the money
            try:
                money = float(input())
                if money <= 0: # if the money is zero or less than zero it will print this message
                    print("Please insert the right amount.")
                    continue
                money_inserted += money
                if money_inserted < product["price"]: # if the money inserted is less than the price it will print a message and will continue to ask the user to insert more until the right amount of money is inserted.  
                    needed = product["price"] - money_inserted
                    print(f"Not enough money. Please add {needed} pesos.")
                else:
                    # update the stock after every purchase
                    product["stock"] -= 1
                    change = money_inserted - product["price"]
                    print(f"Dispensing {product['product name']}... Your change is {change:.2f} pesos.") #.2f means floating point number and two decimal places
                    break
            except ValueError:
                print("Invalid amount. Please try again.") # this will be printed if the user enter an invalid input or a string

        # option for user to enter again or not
        while True:
            repeat = input("Would you like to order again? Yes or No: ").strip().lower() # strip is to remove spaces and lower is to convert the input to lowercases
            if repeat == "yes":
                break
            elif repeat == "no":
                print("Thank you for ordering! Please come back again :)")
                exit()  # exit if the user enters no
            else:
                print("Invalid input. Please type 'Yes' or 'No' only.") # if the user enters anything other than yes or no
    