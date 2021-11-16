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

# you can also put in keywords arguments by adding * in front of the parameter name

def function_with_kwargs(**kwargs):
    print(kwargs['username'])
    print(kwargs['password'])

function_with_kwargs(username='Dro', password='test')

def another_kwarg_function(**kwargs):
    for key, value in kwargs.items():
        print(f'the key is {key} and the value is {value}')

another_kwarg_function(name="Eric", profession="Trainer")


