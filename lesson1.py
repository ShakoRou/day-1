from turtle import *


#we want to paint a house 
#step 1 draw a square

speed(20)
width(7)
color("purple")
begin_fill()
forward(200) #200 aq aris piqselis parametri
left(90) 

forward(200)
left(90) 

forward(200) 
left(90) 

forward(200) 
left(90) 
end_fill()

#end of square

#drawning a door 

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #karebis simagle
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#karebis dasasruli 

#saxuravis dasawyisi 

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#saxuravis dasasruli 

#marcxena panjris dasawyisi 

penup()
goto(50, 130)
pendown()
color("blue")
begin_fill()
right(60)

forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#marcxena panjaris dasasruli 

#marjvena panjris dasawyisi 

penup()
goto(140, 130)
pendown()
color("blue")
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

#marjvena panjris dasasruli 









exitonclick() #es punqcia madzlevs sashualebas shevinarchuno panjara sanam ar davaklikeb
