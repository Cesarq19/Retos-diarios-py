def unique_in_order(iterable):
    if len(list(iterable))>0:
        lista = list(iterable)
        validacion = [lista[0]]
        for i in range(len(lista)-1):
            if lista[i]!=lista[i+1]:
                validacion.append(lista[i+1])
    else:
        validacion=[]
    return validacion

print(unique_in_order('AAAABBBCCDAABBB'))