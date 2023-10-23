# list comprehensions
# [output_variable __collection (iterable)__ conditions]
# a = [1, 2, 3]
# [x for x in a if x != 1]
from random import randint

numbers = list(range(100))
numbers = [even for even in numbers if even % 2 == 0]
print(numbers)

# set comprehension
random_unique_elements = {randint(1, 10) for i in range(10)}
print(f"{random_unique_elements}\nType: {type(random_unique_elements)}")

# Dict comprehensions
random_dictionary = {i: randint(1, 10) for i in range(5)}
print(random_dictionary)

