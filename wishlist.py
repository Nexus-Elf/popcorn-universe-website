import json
import math
import locale
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )
def main():

    itemWishlist = {
    "Bootstrap Studio": 60.00, 
    "Polo G Hoodie" : 59.99, 
    "Placeholder" : 10.00
    }
    subtotal = sum(itemWishlist.values())
    plusTax = (subtotal * 0.065)
    shippingRate = 5.99
    totalPrice = (subtotal + plusTax + shippingRate)
    
    print("Your Order:")
    print("")
    print("Item          Cost")
    print(*itemWishlist.items(), sep='\n')
    print("--------------------")
    print("SUBTOTAL: " + locale.currency(subtotal))
    print("TAX: " + locale.currency(plusTax)) 
    print("SHIPPING: " + locale.currency(shippingRate)) 
    print("TOTAL: " + locale.currency(totalPrice))
    print("Thank You!")
    print("- MGMT")
if __name__ == "__main__":
    pass
main()

