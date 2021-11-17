"""

Dictionaries:
    key value pairs

    Add new properties:
        shorthand [] ~ 2:05
        update method ~ 2:06
        setdefault ~ 2:10

    Get values:
        shorthand [] ~ 2:14
        get method ~ 2:14
        values method ~ 2:15

    Get keys:
        keys method ~ 2:15
"""

dictionary = {
    'name': 'alejandro',
    'age': 18
}


def loop_through_dict(dicti):
    for item in dicti.items():
        print(item)


loop_through_dict(dictionary)
