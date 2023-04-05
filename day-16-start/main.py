# import another_module
# print(another_module.another_variable)

# import turtle
# timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle() 
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.fd(100) 

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "r"
print(table)
