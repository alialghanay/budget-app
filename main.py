from category import Category # Import the class
from create_spend_chart import create_spend_chart # Import the function

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
clothing.deposit(1000, 'deposit')
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category('Auto')
auto.deposit(1000, 'deposit')
auto.withdraw(15)
print(food)


print(create_spend_chart([food, clothing, auto]))