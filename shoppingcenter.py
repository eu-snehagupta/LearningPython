import json
# this function displays the welcome screen to the customer
def welcomeScreen():
    print("Hi. Welcome to our store!")
    print("Here are the stock details--")
    for stock_details in stock['Items']:
        print(stock_details['item_type'] + "\t:\t" + stock_details['cost'] + " " + stock_details['currency'] + "\t:\t" + stock_details['count'] + "pcs.")

Stock = '''
{
    "Items":[
            {
                "item_type":"shirt",
                "code":"001",
                "count": "30",
                "cost": "30",
                "currency":"SEK"
            },
            {
                "item_type":"pant",
                "code":"002",
                "count": "40",
                "cost": "40",
                "currency":"SEK"
            },
            {
                "item_type":"cap",
                "code":"003",
                "count": "20",
                "cost": "20",
                "currency":"SEK"
            },
            {   
                "item_type":"socks",
                "code":"004",
                "count": "10",
                "cost": "10",
                "currency":"SEK"
            }
    ]
}  '''

stock = json.loads(Stock)
# this funtion fetch the cost of the item baised on the input of multiple_order function
def shoplist(x):
    for stock_details in stock['Items']:
        if x == "shirt":
            if(stock_details['item_type']=="shirt"):
                return stock_details['cost']
        elif x == "pant":
            if(stock_details['item_type']=="pant"):
                return stock_details['cost']
        elif x == "cap":
            if(stock_details['item_type']=="cap"):
                return stock_details['cost']
        elif x == "socks":
            if(stock_details['item_type']=="socks"):
                return stock_details['cost']

# this function fetch the order details of the customer
def multiple_order(payment_amount):
    more_order = input("Do you want to place an order?[yes/no]: ").lower()
    
    if more_order == "yes":
        x = input("Enter your order details:").lower()
        return multiple_order(payment_amount + int(shoplist(x)))
    elif more_order == "no":
        return payment_amount 

welcomeScreen()
print("------------------\n Your net amount is :" + str(multiple_order(0)) + "\n-----------------\n")
print("Thank you for choosing our store. Have a nice day!")
