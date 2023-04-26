# EJERCICIO 1

# LEER NÚMERO
numero = int(input('Introduce un número entero: '))

# Esta función recibe un número y devuelve todos los números pares de manera descendiente desde sí mismo 
# hasta el 0 incluido
def funcion_par(valor):
    for i in range(valor, -1, -1):
        print(i)
# Esta función recibe un número y devuelve todos los números impares de manera descendiente desde sí mismo 
# hasta el 1 incluido
def funcion_impar(valor):
    for i in range(valor, 0, -2):
        print(i)

# Esta función recibe un número entero, determina si es par o impar y devuelve otra función
def clasificador_par_impar(numero):
    # si es par ejecutar la función par
    if numero % 2 == 0:
        return funcion_par(numero)
    # si es impar ejecutar la función impar
    else:
        return funcion_impar(numero)

# MOSTRAR RESULTADO
clasificador_par_impar(numero)

