
def vowel_filter(function):

    def wrapper():
        res = function()
        return [el for el in res if el.lower() in 'aiuoey' ]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())