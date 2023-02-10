print("The Invoice Line Item Calculator \n")

def aquirePrice():
    while True:
        try:
            print("Enter price: ", end = "")
            price = float(input())
            return price
        except:
            print("Invalid decimal number. Please try again.")
    
    
def aquireQuantity():   
    while True:
        try:
            print("Enter quantity: ", end = "")
            quantity = int(input())
            return quantity
        except:
            print("Invalid integer. Please try again.")

while True:
    price = aquirePrice()
    quantity = aquireQuantity()
    total = quantity * price
    print("PRICE: \t\t\t" + str(price))
    print("QUANTITY: \t\t" + str(quantity))
    print("TOTAL: \t\t\t" + str(total))
    print("Enter another line item? (y/n): ", end = "")
    answer = input()
    if answer == "y":
        continue
    else:
        print("\nBye!")
        break
