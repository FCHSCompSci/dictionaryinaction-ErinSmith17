#Erin Smith -
#Dictionary Project 9/17/18

def make_cake(c_id,size,shape,flavor):
    cake = {
        'c_id' : cake_id,
        'size' : size,
        'shape' : shape,
        'flavor' : flavor
        }
    return cake

def make_customer(c_id,name):
    customer = {
        'c_id' : cake_id,
        'name' : name
        }
    return customer

cake_id = 0

while True:
    user_input = input("Would you like to order a [c]ake,[p]ickup or [e]xit? ")
    if user_input == "c":
        order_name = input("What is the name for the order? ")
        customer(name).append(order_name)
        cake_id = cake_id + 1
        cake_size = input("What size would you like? ")
        cake_shape = input("What shape of cake would you like? ")
        cake_flavor = input("What flavor of cake would you like? ")
    elif user_input == "p":
        pass
    elif user_input == "e":
        print("Have a nice day!")
        break
