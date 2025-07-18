def get_coffee_price(coffee):
    """
    Returns the price of the coffee.
    :param coffee: the list of coffee
    :return:
    """
    return coffee["price"]

def get_coffee_country(coffee):
    """
    Returns the country of the coffee.
    :param coffee: the list of coffee
    :return:
    """
    return coffee["country"]

def get_coffee_name(coffee):
    """
    Returns the name of the coffee.
    :param coffee:
    :return:
    """
    return coffee["name"]

def set_coffee(coffee,name,country,price):
    """
    Sets the properties of the coffee.
    :param coffee: the coffee to be set
    :param name: the name of the coffee
    :param country: the country of the coffee
    :param price: the price of the coffee
    :return: the coffee with the properties set
    """
    coffee["name"]=name
    coffee["country"]=country
    coffee["price"]=price
    return coffee

def convert_to_string(coffee):
    return "Name: "+get_coffee_name(coffee)+", Country: "+get_coffee_country(coffee)+", Price: "+str(get_coffee_price(coffee))

def add_coffee(coffee:list, prop:list)->list:
    """
    Adds a coffee to the list of coffee.
    :param coffee: The list of coffee
    :param prop: The properties of the coffee
    :return: list of dictionaries containing the coffee
    """
    if float(prop[2])<=0:
        print("The price must be a positive number")
        return
    for i in coffee:
        if get_coffee_name(i)==prop[0]:
            print("The name already exists")
            return
    mini_coffee=set_coffee({}, prop[0], prop[1], float(prop[2]))
    coffee.append(mini_coffee)
    return coffee

def test_add_coffee():
    coffee=[]
    coffee = add_coffee(coffee, ["Macha", "India", "3"])
    assert coffee==[{"name":"Macha", "country":"India", "price":3}]
    coffee = add_coffee(coffee, ["Mocha", "India", "5.3"])
    assert coffee==[{"name":"Macha", "country":"India", "price":3}, {"name":"Mocha", "country":"India", "price":5.3}]

def sorting(coffee):
    """
    Sorts the list of coffee by country and price.
    :param coffee: the initial list of coffee
    :return: list of dictionaries containing the sorted coffee
    """
    coffee.sort(key=lambda x: (x["country"], x["price"]))
    return coffee

def filter_coffee(coffee, country, price):
    """
    Filters the list of coffee by country and price.
    :param coffee: the initial list of coffee
    :param country: the country to filter by
    :param price: the price to filter by
    :return:
    """
    coffee_dup=[]
    for i in range(len(coffee)):
        if get_coffee_country(coffee[i])==country and get_coffee_price(coffee[i])<=price:
            coffee_dup.append(coffee[i])
    return coffee_dup

def filter_coffee_no_price(coffee, country):
    """
    Filters the list of coffee by country.
    :param coffee: the initial list of coffee
    :param country: the country to filter by
    :return:
    """
    coffee_dup=[]
    for i in range(len(coffee)):
        if get_coffee_country(coffee[i])==country:
            coffee_dup.append(coffee[i])
    return coffee_dup

def filter_coffee_no_country(coffee, price):
    """
    Filters the list of coffee by price.
    :param coffee: the initial list of coffee
    :param price: the price to filter by
    :return: the list of coffee filtered by price
    """
    coffee_dup=[]
    for i in range(len(coffee)):
        if get_coffee_price(coffee[i])<=price:
            coffee_dup.append(coffee[i])
    return coffee_dup

def delete_coffee(country, coffee):
    """
    Deletes all the coffee from a given country.
    :param country: the country to delete the coffee from
    :param coffee: the initial list of coffee
    :return: the list of coffee without the coffee from the given country
    """
    coffee_dup=[]
    for i in range(len(coffee)):
        if get_coffee_country(coffee[i])!=country:
            coffee_dup.append(coffee[i])
    return coffee_dup
