#carpe diem

import turtle
import easygui
from datetime import date
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'carpediem_helper.txt')

t = turtle.Turtle()
t.speed("fastest")
t.fillcolor("violet")

file = open(my_file, 'r+')
saved_birthday = file.readline()
#print(saved_birthday)
file.close()
if(saved_birthday == ""):
    user_input = easygui.enterbox("When is your birthday?")
    file = open(my_file, 'w+')
    file.write(user_input)
    file.close()
else:
    user_input = saved_birthday

user_input = user_input.split("-")    

today = date.today()
print("Todays date: ", today)
birthday = date(today.year,int(user_input[0]),int(user_input[1])) 
#print("Birthday date: ", birthday)


delta = today - birthday
days_past = delta.days
if(days_past < 0):
    days_past = 365 + days_past

#print(days_past)

def draw_day(past):
    t.pendown()
    if(past): t.begin_fill()
    t.circle(10)
    if(past): t.end_fill()

    t.penup()
    t.forward(30)

t.penup()
t.setpos(-350,275)

days_drawn = 0
for i in range(19):
    for i in range(19):
        if days_drawn < days_past:
            draw_day(True)
        else:
            draw_day(False)
        days_drawn += 1
    t.setpos(-350, t.ycor() - 30) 
for i in range(4):
    if days_drawn < days_past:
        draw_day(True)
    else:
        draw_day(False)
    days_drawn += 1

t.forward(25)
t.write("Carpediem",font=("Verdana",15,"normal"))
t.hideturtle()

input("")

