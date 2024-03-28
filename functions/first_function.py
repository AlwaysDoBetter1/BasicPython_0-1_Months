"""
Write a function draw_triangle() that draws a star-shaped right triangle with legs equal to 10 as shown:

*
**
***
****
*****
******
*******
********
*********
**********

"""

# function declaration
def draw_triangle():
    for i in range(1, 11):  # draw star triangle
        print(i * '*')

draw_triangle()  # function call