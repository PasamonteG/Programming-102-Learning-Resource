# Define the variables to be used
# They are float to allow to use any type of triangles. Not just the ones with natural number sizes.
base = float(input('Triangle base:'))
height = float(input('Height of the triangle:'))

def triangle_area(b,h): # We need this function to have two arguments
    area = b * h / 2
    return area # We just return the value to be able to do things with it.

print('The area of your triangle is:',triangle_area(base,height))
