menu = {

    "pizza" : 200,
    "pasta" : 100,
    "meggie" : 80,
    "burger" : 120,
    "salad"  : 50,
    "coffee" : 90,
    "tea" : 20,
    "samosa" : 25,
    "kachori" : 40,
    "dabeli" : 35,
    "vadapav" : 40,
    "panipuri" : 50,
    "dosa" : 90,
    "idli" : 50,
    "daal pakwan" : 110,
    "muskabun" : 80,


}

print("Welcome to restaurant!")
print("----------MENU----------")
for item, price in menu.items() :
    print(f"{item :<10} : {price}Rs")

order_total = 0
order_details = {}

while True :
    item = input("Enter the name of item you want to order : ").lower()

    if item in menu :
        qty = int(input("Enter Quantity : "))
        order_total += menu[item] * qty

        if item in order_details :
            order_details[item] += qty
        
        else :
            order_details[item] = qty
        print(f"your item {item} has been added to your order.")

    else :
        print(f"orderd item {item} is not availaible yet.")

    choice = input("do you want to add more item (yes/no) : ").lower()
    if choice == "no" :
        break

print("\n==============RECEIPT==================")
print(f"{'Item' : <12}{'Qty' : <6}{'price' :<8}{'total'}")
print("-" * 40)

for item,qty in order_details.items() :
    price = menu[item]
    total = price * qty
    print(f"{item : <12}{qty : <6}{price : <8}{total}")

print("-" * 40)
print(f"{'Grand Total' : <26}{order_total}Rs")
print("=======================================")
print("THANK YOU!! VISIT AGAIN")