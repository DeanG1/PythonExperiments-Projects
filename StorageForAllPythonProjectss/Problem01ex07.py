# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (текст със следните възможности:
# square, rectangle, circle или triangle).
# •	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# •	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# •	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# •	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната
# му и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая
import math

figure = input()
if figure == "square":
    square_side = float(input())
    square_area = square_side * square_side
    print(f"{square_area:.3f}")
elif figure == "rectangle":
    rectangle_a_side = float(input())
    rectangle_b_side = float(input())
    rectangle_area = rectangle_b_side * rectangle_a_side
    print(f"{rectangle_area:.3f}")
elif figure == "circle":
    radius = float(input())
    circle_area = radius * radius * math.pi
    print(f"{circle_area:.3f}")
elif figure == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    triangle_area = triangle_height * triangle_side / 2
    print(f"{triangle_area:.3f}")