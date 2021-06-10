

# for en listas
for i in range(100):
    print(i)

lista_con_for = [i * 100 for i in range(100)]
# if en listas
i = 100
# para obtener los números pares
[i for i in range(100) if i % 2 == 0]
# para obtener los números impares
# not, !=
[i for i in range(100) if not i % 2 == 0]
[i for i in range(100) if i % 2 != 0]


# else en listas
x = [i if i % 2 == 0 else "No es par" for i in range(100)]

# for usando listas
# a lista anterior sumarle 1 a los números enteros
[i + 1 for i in x if isinstance(i, int)]
[i + 1 for i in x if i % 2 == 0]  # error por tratar de usar módulo con un str
[x[i] + 1 for i in range(len(x)) if i % 2 == 0]

x[0] = "No es par"  # Se equivocaron y en un par pusieron texto!!!!!
[i + 1 for i in x if isinstance(i, int)]
[x[i] + 1 for i in range(len(x)) if i % 2 == 0]


[i + 1 if isinstance(i, int) else x[i] for i in x]  # error
[i + 1 if isinstance(i, int) else i for i in x]
[i if isinstance(i, str) else i + 1 for i in x]
[i if isinstance(i, str) else x[i] + 1 for i in x]

[u for u in x]

[i for i in x]


# [for variable_que_recorre_el_for in objeto_iterable if condicion depende variable_que_recorre_el_for]

activado = False
x = 1 if activado else 0
x

activado = False
[i for i in range(100) if activado]

activado = True
[i for i in range(100) if activado]

[i if activado else 0 for i in range(100)]
activado = False
[i if activado else 0 for i in range(100)]


# promedio


# mediana


# moda


# ordenar


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
menos_minutos = [l_nombres[i] for i in l_dato if l_dato[i] < 26]
print(menos_minutos)

# Crear una lista con los compañeros de horas de sueño promedio
l_nombres2 = l_horas = print(l_horas)

# Mostrar los compañeros que sólo duermen más de 8 horas
l_mas8 = [l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] >= 8]
print(l_mas8)

# Mostrar los compañeros que sólo duermen menos de 8 horas y a los que
# duermen menos 4 sustituir su nombre por vampiro
l_vampiros = [l_nombres2[i] + " es un vampiro" if l_horas[i] <
              4 else l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] < 8]
print(l_vampiros)
