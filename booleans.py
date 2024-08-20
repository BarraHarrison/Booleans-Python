# This means 10 million
population_in_seoul = 10_000_000
population_in_cork = 500_000

yes = True
no = False

if population_in_seoul < 1_000_000:
    print("Seoul is a small city")
else:
    print("Seoul is a sprawling metropolis")
if population_in_cork < 1_000_000:
    print("Cork is a small city")
else:
    print("Cork is a big city in Ireland")

# print(type(yes))
# print(population_in_seoul)


# Write a Python program to add 'ing' to the end of a string.
# Add 'ly' if the word already ends with 'ing'
# if the string length of the given string is less than 3, leave it unchanged

# create function which adds "ing"
def add_ing(word):
    if len(word) < 3:
        return word
    if word.endswith("ing"):
        return word + "ly"
    else:
        return word + "ing"

# Example messages
messages = [
    "pass",        
    "playing",    
    "walk",       
    "swimming",   
    "go",         
    "create",     
    "writing",    
    "try",        
    "fix",        
    "eat"      
]

# applying function
for message in messages:
    result = add_ing(message)
    print(f"Original: {message}/ Modified with Python: {result}")