#use of dictionary and conditional statements 

#define the menu 
menu = {
    'Chocolate Shake' : 40,
    'Margarita Pizza' : 100,
    'Pasta'           : 50,
    'Cheese Sandwich' : 40 ,
    'Burger'          : 60
}

# print(menu)

#Greet the customers 
print("WELCOME TO SNEHA RESTAURANT")

#display the menu
print("Chocolate Shake : Rs40\nMargarita Pizza : Rs100\nPasta : Rs50\nCheese Sandwich : Rs40\nBurger: Rs60" )

#define the variable 
order_total = 0 

#the first order given by user will be stored in item1 variable 
item_1 = input("Enter the name of item you want to order: ")

#check whether the number of item is present in menu or not 
#order total stores the total order given by user 
#menu  is the dictionary 
if item_1 in menu :
    order_total +=menu[item_1] #0+40= 40
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available!")

#orders more order 
another_order  =  input("Do you want to add another item ? (Yes/No)")

#check if user gives another order 
if another_order == "Yes":
    item_2 = input("Enter the name of second item : ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

#total price
print(f"Total amount of items to pay  is {order_total}")

