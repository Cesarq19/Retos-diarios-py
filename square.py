def is_square(n): 
    condicion = False
    if n>=0:
        numero_base = pow(n,0.5)
        n_fijo = int(numero_base)
        diferencia = float(n_fijo)-numero_base
    
        if diferencia == 0.0:
            condicion = True
        else:
            condicion = False
    return condicion

print(is_square(15))