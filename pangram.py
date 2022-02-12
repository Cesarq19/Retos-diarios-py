import string

def is_pangram(s):
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    validacion = list()
    for caracter in s:
        if not caracter.lower() in validacion and caracter.lower() in alfabeto:
            validacion.append(caracter.lower())
        validacion.sort()
    if len(alfabeto) == len(validacion):
        return True
    else:
        return False