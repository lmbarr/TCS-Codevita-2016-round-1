def producto_minimo_dos_arrays(n, k, array1, array2):
    lista_valores = list()
    mayor = 2 * k

    global terminos_iniciales
    terminos_iniciales = [array1[i]*array2[i] for i in range(len(array1))]
    suma_inicial = sum(terminos_iniciales)
    suma_excepto_ese_numero = [suma_inicial-terminos_iniciales[i] for i in range(len(terminos_iniciales))]


    for j in range(len(array1)):
        termino1 = (array1[j] + mayor) * array2[j] + suma_excepto_ese_numero[j]
        termino2 = (array1[j] - mayor) * array2[j] + suma_excepto_ese_numero[j]
        lista_valores.append(termino1)
        lista_valores.append(termino2)

    return producto_minimo(lista_valores)

def producto_minimo(lista_valores):
    return min(lista_valores)
