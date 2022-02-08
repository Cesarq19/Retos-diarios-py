def rot13(message):
    n = 13 # numero de desplazamientos
    abc =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    encrypted = ''
    for caracter in message:
        if caracter.isalpha():
            indice = abc.index(caracter.lower())
            i = indice + n
            if i > 25:
                m = i -26
            else:
                m = i
            if caracter.isupper():
                encrypted += abc[m].upper()
            else:
                encrypted += abc[m].lower()
        else:
            encrypted += caracter
                
    return encrypted