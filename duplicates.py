def duplicate_count(text):
    conteo = 0
    lista = []
    for caracter in text.lower():
        if text.lower().count(caracter)>1 and not caracter in lista:
            lista.append(caracter)
            conteo += 1
    return conteo