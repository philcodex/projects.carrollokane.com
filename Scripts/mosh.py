price = 10
price = 20
name = "Phil"
is_published = True
print(price)

name  = "John Smith"
age = 20
is_new = True
print(name)
print(age)
print(is_new)

name = input('What is your name? ')
print('Hi ' + name)
colour = input('What is your Fav colour? ')
print('Hi ' + name + ' likes ' + colour)

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2026 - int(birth_year)
print(type(age))
print(age)

weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)


course = 'Python for Beginners'
another =  course[:]
print(another)

name = 'Jennifer'
print(name[1:-1])

# Formatted strings

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)

# String methods

course = 'Python for Beginners'
# print(len(course))
print(course.upper())
print(course.lower())
print(course.replace('P', 'J'))
print(course)
print('python' in course)

# Arithmetic operators

print(10 + 3) # addition
print(10 / 3) # division
print(10 // 3) # floor division
print(10 % 3) # modulus
print(10 ** 3) # exponentiation

x = 10
x = x + 3
x += 3
x -= 3
print(x)

x = 10 + 3 * 2
print(x)




