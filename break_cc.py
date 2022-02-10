def solution(s):
    cadena = ''
    for caracter in s:
        if caracter.isupper():
            cadena +=' '+ caracter
        else:
            cadena+= caracter
    return cadena