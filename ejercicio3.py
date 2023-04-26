# LEER HORAS TRABAJADAS Y LEER TARIFA
horas_trabajadas = int(input("Introduce las horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))

# CALCULAR SUELDO BASE Y POR HORAS EXTRAS
if horas_trabajadas > 40:
    horas_extra = horas_trabajadas - 40
    sueldo_base = 40 * tarifa
    sueldo_extra = horas_extra * (tarifa * 1.5)
    sueldo_total = sueldo_base + sueldo_extra
else:
    sueldo_total = horas_trabajadas * tarifa

# MOSTRAR RESULTADO
print(f"El sueldo total es: {sueldo_total}")
