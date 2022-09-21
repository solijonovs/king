############################################################################
# Author: Shohislombek Solijonov
# Username: solijonovs
# Google Doc Web Address:https://docs.google.com/document/d/1Q3o4YX3DvUOurfFumpa1M5_Ieb5dbkoMjDX8yxqxvGM/edit?usp=sharing
# Date: September 19, 2022
############################################################################

import turtle
wn=turtle.Screen()
wn.bgcolor('green')

#turtle #1
abby=turtle.Turtle()
abby.hideturtle()

abby.color('blue')
abby.begin_fill()
for side in range(4):
     abby.left(90)
     abby.forward(50)
abby.end_fill()


#turtle #2
king=turtle.Turtle()
king.hideturtle()

king.color('red')
king.begin_fill()
for side in range(4):
     king.right(90)
     king.forward(50)
king.end_fill()

#writting
king.write("I hope you like it",move=False,align='center',font=("Arial",30,("bold","normal")))

wn.exitonclick()