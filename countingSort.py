def counting (maximo:int, num):    
    #maximo é o numero maximo inserido no array.
    
    contador = (maximo + 1) *[0]
    for y in num:
        contador[y] = contador[y] + 1
    i=0
    for y in range (maximo + 1):
        for j in range(contador[y]):
            num[i] = y
            i = i + 1
    return num

