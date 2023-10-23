def dynamic_args_function(*args, **kwargs):
    """
    Blah Blah.
    :param args:
    :param kwargs:
    :return:
    """
    print(f"*args: {args}\nType of *args: {type(args)}")
    print()
    print(f"**kwargs: {kwargs}\nType of **kwargs: {type(kwargs)}")

#
# dynamic_args_function(1, 2, 3, a="Yohoho", b="Machine Learning", c="Backend and API")

# List Comprehensions
# Generators
