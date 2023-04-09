#허슬러 페인터
import colorgram as cg
import turtle as t
import random as rd
# rgb_colors = []
# colors = cg.extract('day-18-start_hirstPainting/image.jpg', 30)
# for color in colors :
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)   
color_list = [(237, 205, 82), (204, 143, 165), (196, 181, 96), (158, 72, 44), (66, 111, 131), (125, 39, 37), (143, 67, 110), (221, 230, 232), (236, 244, 241), (172, 159, 48), (105, 142, 172), (4, 131, 68), (148, 35, 65), (56, 34, 54), (136, 186, 176), (1, 117, 79), (43, 36, 57), (36, 35, 33), (57, 172, 175), (233, 172, 154), (63, 171, 169), (70, 68, 55), (211, 179, 189), (180, 95, 87), (155, 111, 127), (165, 206, 193), (123, 126, 135), (166, 204, 207)]
t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")

tim.ht()
tim.pu()
pos_x = -300
pos_y = -300
for i in range(10) :
    tim.setpos(pos_x, pos_y)
    for j in range(10) :
        tim.pd()
        tim.dot(20, rd.choice(color_list))
        tim.pu()
        pos_x += 50
        tim.setx(pos_x)
    pos_x = -300
    pos_y += 50

screen = t.Screen()
screen.exitonclick()