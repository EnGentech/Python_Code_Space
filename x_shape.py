import pyinputplus as pyip

def odd(numb):
    numb = int(numb)
    if numb % 2 == 1:
        return numb
    else:
       raise pyip.ValidationException('Error: {} is not an odd number'.format(numb))

height = pyip.inputCustom(customValidationFunc=odd, prompt='Enter height in odd number$ ')

space = 0
inside = height
for x in range(0, height, 2):
    inside -= 2
    if space == (height//2):
        print(" " * space + '*')
    else:
        print(" " * space + '*' + ' ' * inside + '*' + " " * space)
    space += 1
inside = 1
space = height//2 - 1
for z in range(height, 1, -2):
    print(" " * space + '*' + ' ' * inside + '*' + " " * space)
    inside += 2
    space -= 1
