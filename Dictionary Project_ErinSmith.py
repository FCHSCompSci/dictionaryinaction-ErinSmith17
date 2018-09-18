#Erin Smith
#Dictionaary Project 9/17/18

cakes = []
cupcakes = []
pastries = []
orders = cakes + cupcakes + pastries
order = input("Would you like to place an order?: ")

if order == "no":
    print("Thank you, Have a nice day!")
else:
    print("For a cake use the first function, for a cupcake use the second function, and for a pastry use the third function.")
    
    def first(shape,size,flavor):
        cakes = {
            'shape' : shape,
            'size' : size,
            'flavor' : flavor
            }
        cakes.append(cakes)
        return "Your order %s has been placed" % cakes

    def second(size,flavor,frosting):
        cupcakes = {
            'size' : size,
            'flavor' : flavor,
            'frosting' : frosting
            }
        cupcakes.append(cupcakes)
        return "Your order %s has been placed" % cupcakes

    def third(name,flavor,topping):
        pastry = {
            'name' : name,
           'flavor' : flavor,
            'topping' : topping
            }
        pastries.append(pastry)
        return "Your order 5s has been placed" % pastry
else:
    print("Your order is %s") % orders 

