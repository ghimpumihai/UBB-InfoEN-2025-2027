from src.functions import *

def menu():
    print("1.Add coffee")
    print("2.Display all coffees")
    print("3.Filter coffee based on price and country of origin")
    print("4.Delete all coffees from a given country")

def display_all(coffee):
    sorted_coffee = sorting(coffee)
    for i in range(len(sorted_coffee)):
        print(convert_to_string(sorted_coffee[i]))

def print_filter(coffee,country, price):
    if country=="":
        coffee_dup = filter_coffee_no_country(coffee, price)
    elif price=="":
        coffee_dup = filter_coffee_no_price(coffee, country)
    else:
        coffee_dup = filter_coffee(coffee, country, price)
    if len(coffee_dup)==0:
        print("No such coffees")
    else:
        for i in range(len(coffee_dup)):
            print(convert_to_string(coffee_dup[i]))


def main():
    menu()
    test_add_coffee()
    coffee =[
        {"name":"Capuccino", "country":"India", "price":3.5},
        {"name":"Latte", "country":"Italy", "price":4.5},
        {"name":"Mocha", "country":"India", "price":5.3},
             ]
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            prop= input("Enter the properties of the coffee: ")
            prop = prop.split(" ")
            coffee=add_coffee(coffee, prop)

        elif choice == '2':
            display_all(coffee)

        elif choice == '3':
            prop=input("Enter the country and price: ")
            prop=prop.split(" ")
            if len(prop)==2:
                print_filter(coffee, prop[0], int(prop[1]))
            else:
                try:
                    x=float(prop[0])
                    print_filter(coffee, "", x)
                except ValueError:
                    print_filter(coffee, prop[0], "")

        elif choice == '4':
            country=input("Enter the country: ")
            coffee=delete_coffee(country, coffee)
main()