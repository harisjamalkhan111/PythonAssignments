import turtle
import math                          

def circle(r):    
    turtle.up()
    turtle.goto(0,r) # go to (0, radius)
    turtle.down() # pen down
    times_y_crossed = 0
    x_sign = 1.0
    while times_y_crossed <= 1:
        turtle.forward(2*math.pi*r/360.0) # move by 1/360
        turtle.right(1.0)
        x_sign_new = math.copysign(1, turtle.xcor())        
        if(x_sign_new != x_sign):
            times_y_crossed += 1
        x_sign = x_sign_new
    turtle.up() # pen up
    return


#enter the radius of the circle 
circle(50)