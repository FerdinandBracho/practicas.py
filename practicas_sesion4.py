
#! Ejercicio 1 
suma = lambda x, y: str(x) + str(y) if (isinstance(x, str) or isinstance(y, str))  else x+y
print(suma(1, '2'))

#! Ejercicio 2 

    # !2.1
user = {    
    'key': 'value'
}

extract = lambda dic : print(f'La llave es: {list(dic.keys())[0]} y el valor es {dic.get(list(dic.keys())[0])}')
extract(user)

    # !2.2
cel = {
    'brand': 'apple',
    'model': 8,
    'status': 'workin'
}

cel['model'] = cel['model'] + 10

# !Ejercicio 3 

