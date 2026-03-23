# ============================================
# 01_datatypes - Practice Exercises
# ============================================

# Exercise 1
# Create variables of type int, float, str and bool
# Print each variable and its type
a = 10
b = 3.14
c = "Hello"
d = True

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))   


# Exercise 2
# Create two variables - your name and age
# Print: "My name is ___ and I am ___ years old" (without fstring)
name = "Nivedita"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old")


# Exercise 3
# Create a variable with value "123"
# Convert it to int and multiply by 2
# Print the result
num_str= "123"
result = int(num_str) * 2     
print(result)


# Exercise 4
# Create a variable with value 9.99
# Convert it to int
# Print the result and explain what happened to the decimal
float_num= 9.99
result = int(float_num)
print(result)
# The decimal part is truncated when converting a float to an int, so we only get the whole number part, which is 9 in this case.

# Exercise 5
# Try converting "hello" to int
# Handle the ValueError using try/except
# Print "Cannot convert to int!" when error occurs
a = "hello"
try:
    result = int(a) 
except ValueError:
    print("Cannot convert to int!")