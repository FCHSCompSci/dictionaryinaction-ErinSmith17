#Erin Smith - Dictionary Project
#9/17/18- 9/24/18

order =[]
def make_cake(cake_id,size,shape,flavor):
    cake = {
        'c_id' : cake_id,
        'size' : size,
        'shape' : shape,
        'flavor' : flavor
        }
    return cake

def make_customer(cake_id,name):
    customer = {
        'c_id' : cake_id,
        'name' : name
        }
    return customer

cake_id = 0

while True:
    user_input = input("Would you like to order a [c]ake,[p]ickup or [e]xit? ")
    if user_input == "c":
        order_name = input("What is the name for the customer order? ")
        cust = make_customer(cake_id, order_name)
        cake_id = cake_id + 1
        order_size = input("What size would you like? ")
        order_shape = input("What shape of cake would you like? ")
        order_flavor = input("What flavor of cake would you like? ")
        whole = make_cake(cake_id, order_size, order_shape, order_flavor)
        print("Your order has been placed, thank you!")
    elif user_input == "p":
        pass
    elif user_input == "e":
        print("Have a nice day!")
        break
#need help figuring out how to append each input to the dictionary
#every time i put order_size == make_cake('size') it says that the
#other positional arguments are missing but im doing the other requirement below
