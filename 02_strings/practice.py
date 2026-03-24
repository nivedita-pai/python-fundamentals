# ============================================
# 02_strings - Practice Exercises
# ============================================

# Exercise 1
# Create a variable with your full name
# Print the total number of characters in it
name ="Nivedita Gajesh"
print("Total characters in the name:", len(name))


# Exercise 2
# Given string: "  Hello Python  "
# Remove the spaces and print in uppercase
sentence = "  Hello Python  "
print(sentence.strip().upper())


# Exercise 3
# Given string: "Nivedita"
# Print the following using slicing:
# - First 4 characters
# - Last 4 characters
# - Every alternate character
# - Reversed string
name="Nivedita"
print("First 4 characters:",name[0:4])
print("Last 4 characters:",name[-4:])
print("Every alternate character:",name[::2])
print("Reversed string:",name[::-1])



# Exercise 4
# Given string: "I love Java and Java is great"
# - Count how many times "Java" appears
# - Replace "Java" with "Python"
# - Check if it starts with "I"
# - Check if it ends with "great"
sentence = "I love Java and Java is great"
print("Count of 'Java':", sentence.count("Java"))
print("After replacement:", sentence.replace("Java", "Python"))
print("Starts with 'I':", sentence.startswith("I"))
print("Ends with 'great':", sentence.endswith("great"))



# Exercise 5
# Given string: "2024-03-23"
# Split it by "-" and print day, month, year separately
date_string = "2024-03-23"
date_parts = date_string.split("-")
print("Date : ", date_parts[2])
print("Month : ", date_parts[1])
print("Year : ", date_parts[0]) 


# Exercise 6
# Create variables - name, city, language
# Print this using f-string:
# "Hi I am ___, from ___, and I love ___!"

name,city,language = "Nivedita","Pune","Python"
print(f"Hi I am {name}, from {city}, and I love {language}!")

# Exercise 7
# Given string: "hello world"
# Capitalize only the first letter of each word
sentence = "hello world"
capitalized_sentence = sentence.title()
print(capitalized_sentence)