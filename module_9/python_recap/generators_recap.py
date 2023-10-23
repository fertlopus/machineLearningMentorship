numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_generator = (number for number in numbers if number % 2 == 0)

# print(type(even_generator))

even = list(even_generator)
even_two = list(even_generator)

# print(even)
# print(even_two)


def even_number_generator(max):
    for i in range(2, max + 1):
        if i % 2 == 0:
            yield i


even = list(even_number_generator(10))
print(even)
