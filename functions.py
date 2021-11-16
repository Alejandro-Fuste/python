# def basic_function_with_params(num_1, num_2):
#     return num_1 + num_2
#
# print(basic_function_with_params(3,4))

# type annotations
# def function_with_type_annotations(number_1: int, number_2: int) -> int:
#     return number_1 + number_2
#
# print(function_with_type_annotations('one', 'two'))

# python varargs

def function_with_vararg(*args: int) -> int:
    value = 0
    for num in args:
        value += num
    return value


print(function_with_vararg(1, 2, 3, 4))
# print(function_with_vararg(1, 2, 'three', 4)) your interpreter will try to run this, but will give type error
