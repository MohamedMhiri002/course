# import colorgram
#
# colors = colorgram.extract('damien-hirst-severed-spots.jpg', 30)
# rgb_colors = []
# for color in colors:
#     new_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(new_tuple)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
list_of_colors = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100



for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(list_of_colors))
    tim.forward(50)

    #draw another line
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()