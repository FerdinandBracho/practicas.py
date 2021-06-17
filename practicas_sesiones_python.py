
# ?Practicas Sesion 1 
# !Crea un string 
string_test = 'Ferdinand'

# !Mostrar posiciones pares 
for i in range(len(string_test)):
    if i % 2 == 0:
        print(string_test[i])

# !Mostrar las tres primeras letras
print(string_test[:3])

# !Concatenar el texto con el mismo 
string_test += string_test
print(string_test)

# !Girar el texto 'Anita lava la tina'
text_to = 'Anita lava la tina'
text_to = text_to[::-1]
print(text_to)

# !Crea una variable llamda nombre y guarda tu nombre, 
# !modifica la variable para que se repita tu nombre, 
# !crea un variable plana y alamcena 100 veces tu nombre, 
# !crea una lsita que tenga 100 elmentos cada uno es tu nombre 
name = 'ferdinand'
name = name * 2
print(name)
plana = [(name[0:10] + ',')]* 100
print(plana)

# !Crea una lista - Accede al valor de la lista - Cambia el elemento de una lista

list_test = ['element 1', 2, 3.0, [4, 'element 4.1']]
print(list_test[2])
list_test[3][1] = 'Prubea cambio'
print(list_test)

# ?Practicas Sesion 2 
# !Convertir los elementos de la lista (Lista = [10,1,2,3,4]) en string 
lista = [10,1,2,3,4]
lista_str = [str(item) for item in lista]
print(lista_str)

# !Obtener el tipo de valor de cada item de la lista 
for item in lista:
    print(type(item))

# ?Practicas sesion 3
# !1 Crear dos variables que representen dos productos, asignarle un precio
masajeador = 2299
candado_moto = 899

# !1.2 Aplicarle iva (16% adicional del precio)
productos = (masajeador, candado_moto)
iva = 16
precio_sin_iva = masajeador + candado_moto
precio_iva = list(map(lambda producto: producto * (iva/100), productos))
impuesto = precio_iva - precio_sin_iva

print(f'El precio de ambos productos sin iva es: {precio_sin_iva}')
print(f'El precio de ambos procuctos con iva es: {precio_iva}')

# !1.3 Calcular el precio total de una pieza por producto
masajeador_iva = productos[0]+precio_iva[0]
candado_iva = productos[1]+precio_iva[1]

print(f'El precio de un masajeador con iva es: {masajeador_iva}')
print(f'El precio de un candado con iva es: {candado_iva}')

print(candado_iva)
print(masajeador_iva)

# !1.4 Calcular el precio total de 4 pieza del producto 1 y 5 del producto 2
print(f'El precio de 4 masajeadores con iva es de: {masajeador_iva * 4}')
print(f'El precio de 5 candados para moto con iva es de: {candado_iva * 5}')

# !1.5 Aplicar 2 operaciones con entero
print(int(masajeador))

# !1.6 Aplicar 2 operaciones con flotantes
print(float(candado_iva))

# !1.7 Aplicar 2 operaciones con strings
print(f'Estos son los precios de los productos {masajeador} y {candado_moto}')

# ! 2 Resuelve las diferentes operaciones con la siguiente lista 
x = list(range(100))
x.extend([50, 50, 50, 50])

# !2.1promedio
promedio = 0
for i in x:
    promedio += i / len(x)
print(f'El promedio de la lista dada es: {promedio}')

# !2.2ordenar
x.sort()
print(x)

# !2.3mediana
mediana = len(x) // 2
print(f'La mediana de la lista dada es : {x[mediana]}')

# !2.4moda
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

# !3 Crear una lista (l_nombres) con los nombres de 5 compañeros
l_nombres = ['antonio', 'aaron', 'yair', 'rosa', 'ferdinand']
print(l_nombres)

# !3.1 Crear una lista (l_dato) con el tiempo que tardan a llegar el trabajo o edad
l_dato = [50, 40, 20, 10, 0]
print("minutos", l_dato)

# !3.3 Cambiar el tiempo (edad) del 3er compañero
l_dato[2] = 30

# !3.4Mostrar los compañeros con menos de 26 años (minutos)
print([l_nombres[i] for i in range(len(l_dato)) if l_dato[i] <= 25])

# !3.5Crear una lista con los compañeros de horas de sueño promedio
l_nombres2 = ['victor', 'carlos', 'osmar']
l_horas = [6, 9, 10]
print(l_horas)

# !3.6Mostrar los compañeros que sólo duermen más de 8 horas
l_mas8 = [l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] >= 8]
print(l_mas8)

# !3.7 Mostrar los compañeros que sólo duermen menos de 8 horas y a los que
l_vampiros = [l_nombres2[i] + " es un vampiro" if l_horas[i] <
              4 else l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] < 8]
print(l_vampiros)

# ?Practicas sesion 4 
# !1 Crea una lambda que tome dos argumentos y los sume no importa si es numerico o string 
suma = lambda x, y: str(x) + str(y) if (isinstance(x, str) or isinstance(y, str))  else x+y
print(suma(1, '2'))

# !2 Ejercicio con diccionarios 
user = {    
    'key': 'value'
}

# !2.1
extract = lambda dic : print(f'La llave es: {list(dic.keys())[0]} y el valor es {dic.get(list(dic.keys())[0])}')
extract(user)

# !2.2
cel = {
    'brand': 'apple',
    'model': 8,
    'status': 'workin'
}

cel['model'] = cel['model'] + 10

# !3 Crear dos listas, una con nombres de companedores y otra con sus posibles alturas 
list_names = ['arturo', 'yair', 'rosy']
list_heights = [170, 160, 160 ]

# !3.1Devuelve con el uso de list comprehension los que midan menos de 165
result = [list_names[x] for x in range(len(list_heights)) if list_heights[x] < 165]
print(result)

# !3.2 Adivina quien 
backend = {'Yair', 'Ferdinand', 'Antonio','osmar'}
frontend = {'Rosy', 'osmar','ferdinand','victor'}
chilangos = {'victor'}
todos = set.union(backend, frontend, chilangos)
no_chilangos = todos - chilangos

dev = {
    'chilango' : False,
    'frontend' : False,
    'backend' : True
}

if dev['chilango']:
    if dev['frontend']:
        print('Eres Victor')
    elif dev['backend']:
        print('Quien eres????')
else:
    if dev['frontend']:
        print('El dev puede ser: Rosy, osmar, Ferdinand, victor')
    elif dev['backend']:
        print('El dev puede ser: Yair o Ferdinand o Antonio o Osmar')    

# ?Practicas sesion 5 
# !Dicionarios que vamos a cargar con un nombre de koder como llave y los minutos que tarda en llegar 
# !a su traajo como valor de esa llave, lluego imprmimos formateado el nombre del koder con 
# !los minutos que tarde en llegar 
nuevo_dict = {}

while True:
    nombre = input('Ingresa un nombre de Koder: ')

    if nombre == 'NO':
        break

    if nombre in nuevo_dict.keys():
        print('Ingresa otro Koder. Ese nombre ya esta registrado!!!')
        continue

    minutos = int(input('Ingresa un numero de minutos: '))
    nuevo_dict.update({nombre: minutos})

for nombre, minutos in nuevo_dict.items():
    print(f'El Koder {nombre} tarda {minutos} minutos en llegar a su trabajo') 

# ?Practicas sesion 6
# !Definir una funcion que reciba multiples valores (numero indefinido) y los sume 
def suma_multiple(*x):
    resultado = 0
    for item in x:
        resultado += item
    return resultado

suma_multiple(1,2,3,4,5,1000)

# ?Practicas sesion 7
# !Funciones recurisvas 

def sum_recursiva(n):
    if n == 0:
        return(n)
    else:
        return(sum_recursiva(n - 1) + n)

sum_recursiva(9)

# !Funcion que reciba dos listas, una con precios de productos, otra con cuantosse compraron, procesar lo necesario para regrar total y sibtotal (+iva 16%)
def totales(precios_fun_sin_iva, cantidad_fun_productos):
    if (len(precios_fun_sin_iva) != len(cantidad_fun_productos)):
        print('Los datos estan incompletos, porfavor revisa las entradas...')
        return
    subtotal = 0
    total = 0
    impuesto = 0
    iva = .16
    for precios, cantidad in zip(precios_fun_sin_iva, cantidad_fun_productos):
        subtotal_aux = precios * cantidad
        subtotal += subtotal_aux
    impuesto = subtotal * iva
    impuesto = '{:.1f}'.format(impuesto)
    total += subtotal + float(impuesto)
    print(f'El precio sin iva de los productos es ${subtotal}, el impuesto agregado es de ${impuesto} dando un total de: ${total}')

totales([10,20], [1,3])

# ? Practicas sesion 8
# !Crar un objeto de tu comida favorita (con dos atributos y con dos metodos)
class FavoriteMeal(object):
    estado = 'Listo'
    temperatura = 'Caliente'
    def comer(self):
        print('Estas comiendo tu comida')
    def guardar(self):
        print('Guardando la comida')

asado = FavoriteMeal()
asado.comer()
asado.guardar()

# !usar self.i como contador
class Acumulador(object):
    def __init__(self):
        self.actual = 0
    def sumar_una_unidad(self):
        self.actual += 1
    def resta_una_unidad(self):
        self.actual -= 1
    def mostar_acumulador(self):
        print(self.actual)

i = Acumulador(2)
i.mostar_acumulador()
i.sumar_una_unidad()
i.resta_una_unidad()

# ! Ejercicio en clase crea el objeto producto, 
# ! a partir de diferentes metodos crea las siguientes acciones:
# ! Definir un precio sin iva inicial del producto (Constructor) 
# ! Modificar el precio actual del producto 
# ! Comprar el MISMO producto y agregar al carrito 
# ! Mostrar precio con iva del producto 
# ! Mostrar el impuesto, subtotal y total de la cantidad de productos agregados al carrito

class Producto(object):
    def __init__(self, nombre, precio = 0):
        self.nombre = nombre
        self.precio_incial = precio
        self.calcular()

    def cambiar_precio(self, nuevo_precio):
        self.precio_incial = nuevo_precio
        self.calcular()

    def calcular(self):
        self.impuesto = self.precio_incial * 0.16
        self.precio_iva = self.precio_incial + self.impuesto

produtest = Producto('cel', 20)
produtest.nombre

class Carrito(object):
    def __init__(self):
        self.precio_total = 0
        self.productos_todos = []

    def agregar_producto(self, producto, cantidad):
        self.precio_total += producto.precio_iva * cantidad
        print(self.precio_total)
        self.productos_todos.append(producto.nombre)

    def limpiar_carrito(self):
        self.productos_todos = []
        self.precio_total = 0
        print(self.precio_total)

    def mostras_contenido(self):
        print(self.productos_todos)
        print(self.precio_total)
    

carritest = Carrito()
carritest.agregar_producto(produtest,1)
carritest.limpiar_carrito()
carritest.mostras_contenido()

