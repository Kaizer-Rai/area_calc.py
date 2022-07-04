def r_calc(length, width):
    area_r = int(length) * int(width)
    print('area of rectangle:', area_r)
def t_calc(height, base):
    area_t = (int(height) * int(base))/2
    print('area of trangle: ', area_t)
def c_calc_rad(rad_dia):
    area_c = 3.14 * int(rad_dia)**2
    print('area of circle: ', area_c)
def c_calc_dia(rad_dia):
    area_c = 3.14 * (int(rad_dia)/2)**2
    print('area of circle: ', area_c)
def sq_calc(side):
    sq_area = int(side)**2
    print('area of square: ', sq_area)
#choices // area_calc.py
while True:
    choice = input('select either rectangle, triangle, square, or circle to calculate area (enter quit to exit): ')
    if choice == 'triangle':
        height = input('input height: ')
        base = input('input base: ')
        t_calc(height, base)
    elif choice == 'rectangle':
        length = input('input length: ')
        width = input('input width: ')
        r_calc(length, width)
    elif choice == 'circle':
        choice_c = input('radius or diameter: ')
        if choice_c == 'radius':
            rad_dia = input('input radius: ')
            c_calc_rad(rad_dia)
        elif choice_c == 'diameter':
            rad_dia = input('diameter: ')
            c_calc_dia(rad_dia)
        else:
            print('input error, try again')
            continue #i want this to loop back 'cirlce or raidus, not tri/rec/circ'
    elif choice == 'square':
        side = input('side length: ')
        sq_calc(side)
    elif choice == 'quit':
        break
    else:
        print('input error, try again')
