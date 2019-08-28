# Function that accepts the dimensions of a triangle and returs its area
def area_triangle(b,h):
    area = b * h / 2
    return area

# After defining the function we introduce the values and invoke it
base = float(input('Base of the triangle: '))
height = float(input('Height of the triangle: '))
print('the area of the triangle is %f squared units' % (area_triangle(base,height))) # %f allows us inserting the float value in the middle of the sentence
