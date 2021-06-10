# 1 Crear dos variables que representen dos productos, asignarle un precio
masajeador = 2299
candado_moto = 899

# 2 Aplicarle iva (16% adicional del precio)
productos = (masajeador, candado_moto)
iva = 16
precio_sin_iva = masajeador + candado_moto
precio_iva = list(map(lambda producto: producto * (iva/100), productos))
impuesto = precio_iva - precio_sin_iva

print(f'El precio de ambos productos sin iva es: {precio_sin_iva}')
print(f'El precio de ambos procuctos con iva es: {precio_iva}')

# 3 Calcular el precio total de una pieza por producto
masajeador_iva = productos[0]+precio_iva[0]
candado_iva = productos[1]+precio_iva[1]

print(f'El precio de un masajeador con iva es: {masajeador_iva}')
print(f'El precio de un candado con iva es: {candado_iva}')

print(candado_iva)
print(masajeador_iva)

# 4 Calcular el precio total de 4 pieza del producto 1 y 5 del producto 2
print(f'El precio de 4 masajeadores con iva es de: {masajeador_iva * 4}')
print(f'El precio de 5 candados para moto con iva es de: {candado_iva * 5}')

# 5 Aplicar 2 operaciones con entero


# 6 Aplicar 2 operaciones con flotantes


# 7 Aplicar 2 operaciones con strings

# ? ////////////////////////////////////////////////////////////////////////////

x = list(range(100))
x.extend([50, 50, 50, 50])

# !promedio
promedio = 0
for i in x:
    promedio += i / len(x)
print(f'El promedio de la lista dada es: {promedio}')

# !ordenar
x.sort()
print(x)

# !mediana
mediana = len(x) // 2
print(f'La mediana de la lista dada es : {x[mediana]}')

# !moda
moda = 0
conteo_moda = 0
for i in x:
    conteo = x.count(i)
    print(conteo)
    valor = i
    print(valor)
    if conteo > conteo_moda:
        conteo_moda = conteo
        moda = valor

print(f'La moda de la lista data es: {moda}')

# ? ////////////////////////////////////////////////////////////////////////////

# 8 Crear una lista (l_nombres) con los nombres de 5 compañeros
l_nombres = ['antonio', 'aaron', 'yair', 'rosa', 'ferdinand']
print(l_nombres)

# 9 Crear una lista (l_dato) con el tiempo que tardan a llegar el trabajo
# o edad
l_dato = [50, 40, 20, 10, 0]
print("minutos", l_dato)

# 10 Cambiar el tiempo (edad) del 3er compañero
l_dato[2] = 30

# Mostrar los compañeros con menos de 26 años (minutos)
print([l_nombres[i] for i in range(len(l_dato)) if l_dato[i] <= 25])

# Crear una lista con los compañeros de horas de sueño promedio
l_nombres2 = ['victor', 'carlos', 'osmar']
l_horas = [6, 9, 10]
print(l_horas)

# Mostrar los compañeros que sólo duermen más de 8 horas
l_mas8 = [l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] >= 8]
print(l_mas8)

# Mostrar los compañeros que sólo duermen menos de 8 horas y a los que
# duermen menos 4 sustituir su nombre por vampiro
l_vampiros = [l_nombres2[i] + " es un vampiro" if l_horas[i] <
              4 else l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] < 8]
print(l_vampiros)
