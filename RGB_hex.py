def rgb(r, g, b):
    valores = [r,g,b]
    respuesta = ""
    for valor in valores:
        if valor <=0:
            respuesta += "00"
        elif valor >= 255:
            respuesta += "FF"
        elif valor>0 and valor<10:
            respuesta += "0"+format(valor,"X")
        else:
            respuesta += format(valor,"X")
    return respuesta