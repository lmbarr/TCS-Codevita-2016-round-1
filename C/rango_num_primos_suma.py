
def esPrimo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def suma_menor_N_lento(N):
    lista_primos_N = [x for x in range(3, N) if esPrimo(x)]#q comience en 3
    #print lista_primos_N
    suma = 2
    contador = 0
    for num_primo in lista_primos_N:
        suma = suma + num_primo

        if esPrimo(suma) and suma <= N:
            #print "suma", suma
            contador = contador + 1
        elif suma > N:
            break

    print contador


def get_primes(number):
    while True:
        if esPrimo(number):
            yield number
        number += 1


def suma_menor_N(N):
    suma = 2
    contador = 0
    gen = get_primes(3)

    def f(suma, contador):
        if suma > N:
            return suma, contador
        else:
            next_num_primo =  next(gen)
            return (f(suma + next_num_primo, contador+1 if esPrimo(suma + next_num_primo) else contador))

    return (f(suma, contador))
