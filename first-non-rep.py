def first_non_repeating_letter(string):
    for caracter in string:
        if string.lower().count(caracter.lower()) == 1:
            return caracter
    return ""