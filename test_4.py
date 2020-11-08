import json
import math
import locale
import sys
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )
def main():

    itemWishlist = {
    "Bootstrap Studio": 60.00, 
    "Polo G" : 59.99, 
    "Placeholder" : 10.00
    }
    subtotal = sum(itemWishlist.values())
    plusTax = (subtotal * 0.065)
    shippingRate = 5.99
    totalPrice = (subtotal + plusTax + shippingRate)
    sorted_items = sorted(itemWishlist.items(), key=lambda e: e[1], reverse=True)
    
    print("Your Order:")
    print("")
    print("Item          Cost")
    print('\n'.join('{}  {}'.format(k, locale.currency(int(v))) for k, v in sorted_items))
    print("--------------------")
    print("SUBTOTAL: " + locale.currency(subtotal))
    print("TAX: " + locale.currency(plusTax)) 
    print("SHIPPING: " + locale.currency(shippingRate)) 
    print("TOTAL: " + locale.currency(totalPrice))
    print("Thank You!")
    print("- MGMT")
    boolprint = input("Would you like to print this receipt? ")
    if boolprint == 'Yes':
        print("Downloading File...")
        sys.stdout = open("receipt.txt", "w")
        print("Your Order:")
        print("")
        print("Item         Cost")
        print("Bootstrap Studio  $60.00")
        print("Polo G Hoodie $59.99")
        print("Placeholder $10.00")
        print("--------------------")
        print("SUBTOTAL: $129.99")
        print("TAX: $8.45")
        print("SHIPPING: $5.99")
        print("TOTAL: $144.43")
        print("Thank You!")
        print("- MGMT")
        sys.stdout.close()
    elif boolprint == 'yes':
        print("Downloading File...")
        sys.stdout = open("receipt.txt", "w")
        print("Your Order:")
        print("")
        print("Item         Cost")
        print("Bootstrap Studio  $60.00")
        print("Polo G Hoodie $59.99")
        print("Placeholder $10.00")
        print("--------------------")
        print("SUBTOTAL: $129.99")
        print("TAX: $8.45")
        print("SHIPPING: $5.99")
        print("TOTAL: $144.43")
        print("Thank You!")
        print("- MGMT")
        
    else:
       print("Ok, Have a nice day!")
if __name__ == "__main__":
    pass
main()
