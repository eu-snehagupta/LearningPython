import json
#FUNCTION DEFINATIONS
def welcomeScreen():
    print("Hi. Welcome to our store!")
    print("Here are the stock details--")
    for stock_details in stock['Items']:
        print(stock_details['item_type'] + "\t:\t" + stock_details['cost'] + " " + stock_details['currency'] + "\t:\t" + stock_details['count'] + "pcs.")

Stock = '''
{
    "Items":[
            {
                "item_type":"Shirt",
                "code":"001",
                "count": "30",
                "cost": "30",
                "currency":"SEK"
            },
            {
                "item_type":"Pant",
                "code":"002",
                "count": "40",
                "cost": "40",
                "currency":"SEK"
            },
            {
                "item_type":"Cap",
                "code":"003",
                "count": "20",
                "cost": "20",
                "currency":"SEK"
            },
            {   
                "item_type":"Socks",
                "code":"004",
                "count": "10",
                "cost": "10",
                "currency":"SEK"
            }
    ]
}  '''

stock = json.loads(Stock)

def shoplist(x):
    for stock_details in stock['Items']:
        if x == "Shirt":
            if(stock_details['item_type']=="Shirt"):
                return stock_details['cost']
        elif x == "Pant":
            if(stock_details['item_type']=="Pant"):
                return stock_details['cost']
        elif x == "Cap":
            if(stock_details['item_type']=="Cap"):
                return stock_details['cost']
        elif x == "Socks":
            if(stock_details['item_type']=="Socks"):
                return stock_details['cost']

def multiple_order(payment_amount):
    more_order = input("Do you want to place an order?[Yes/No]")
    
    if more_order == "Yes":
        x = input("Enter your order details:")
        return multiple_order(payment_amount + int(shoplist(x)))
    elif more_order == "No":
        return payment_amount 

welcomeScreen()
print("------------------\n Your net amount is :" + str(multiple_order(0)) + "\n-----------------\n")
print("Thank you for choosing our store. Have a nice day!")
