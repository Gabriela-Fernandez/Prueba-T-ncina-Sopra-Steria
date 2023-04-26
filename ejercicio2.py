# EJERCICIO 2

# LEER PERSONAS
personas = []
num_personas = 5
for i in range(num_personas):
    sexo = input(f'Introduce el sexo de la persona(masculino/femenino) {i+1}: ')
    edad = int(input(f'Introduce la edad de la persona {i+1}: '))
    personas.append({'sexo': sexo, 'edad': edad})

# CLASIFICAR PERSONAS
contador_mayores = 0
contador_menores = 0
contador_hombres_mayores = 0
contador_mujeres_menores = 0
total_mujeres = 0

for persona in personas:
    if persona['edad'] >= 18:
        contador_mayores += 1
        if persona['sexo'] == 'masculino':
            contador_hombres_mayores += 1
    else:
        contador_menores += 1
        if persona['sexo'] == 'femenino':
            contador_mujeres_menores += 1

for persona in personas:
    if persona['sexo'] == 'femenino':
        total_mujeres += 1

porcentaje_mayores = contador_mayores / len(personas) * 100
porcentaje_mujeres = total_mujeres / len(personas) * 100

# MOSTRAR RESULTADO
print(f'Personas mayores de edad: {contador_mayores}')
print(f'Personas menores de edad: {contador_menores}')
print(f'Hombres mayores de edad: {contador_hombres_mayores}')
print(f'Mujeres menores de edad: {contador_mujeres_menores}')
print(f'Porcentaje de mayores de edad respecto al total: {porcentaje_mayores}')
print(f'Porcentaje de mujeres respecto al total: {porcentaje_mujeres}')


