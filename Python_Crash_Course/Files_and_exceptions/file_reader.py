#open() function retuns an object representing the file 
# python assigns this object to file_object
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)