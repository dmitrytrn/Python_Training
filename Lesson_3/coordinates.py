coord_x = float(input('Enter the X coord -> '))
coord_y = float(input('Enter the Y coord -> '))

if coord_x > 0 and coord_y > 0:
    print('I Quadrant')
elif coord_x < 0 and coord_y > 0:
    print('II Quadrant')
elif coord_x < 0 and coord_y < 0:
    print('III Quadrant')
elif coord_x > 0 and coord_y < 0:
    print('IV Quadrant')
elif coord_x == 0 and coord_y == 0:
    print('Zero Point')
elif coord_x == 0:
    print('Point on O-X beam')
else:
    print('Point on O-Y beam')
