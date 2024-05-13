
#Funciones: Grupo de sentencias agrupadas de tal forma que pueden ser invocadas por un mismo nombre
#Sintaxis básica de una función: 
#def nombre_de_la_función(arg1, arg2,...argN):
#     sentencias (es el cuerpo de la función, consiste en un grupo de senetencias a ejecutar)
#     print 
#Llamar a la función: nombre_de_la_función(contenido arg1, contenido arg2,...contenido argN)
#Ejemplos:
def suma (a,b):
    print(a+b)
suma(2,3)
suma(2.7, 4.0) #Los datos soportan polimorfismo, es decir, saben cómo comportarse ante una gran variedad de operadores
def en_pantalla(frase1, frase2):
    print(frase1,frase2)
en_pantalla('Me guta', 'Python')

#Funciones anidadas: es posible crear funciones dentro de funciones. Ejemplo:
def f1(a): #Función que encierra a f2
    print(a)
    b=100
    def f2(x): #Función anidada en f1
        print(x)
    f2(b)
f1('Python')

#Namespace: Lugar donde residen un conjunto de nombres. El namescape define su ámbito (scope)
#1.Variables que se crean en un módulo (fichero) son globales para ese fichero
#2.Variables asigndas dentro de un función son locales
#Para buscar los nombres Python utiliza la regla LEGB

G='Esta variable es de ámbito Global'
def f3():
    E='Esta variable es local a f3. Enclosing f4'
    def f4():
        L='Esta variable es local a f4'
        print (L, E, G, sep='\n')
    f4()
f3()

#Argumentos. Para pasar argumentos a una función se puede hacer de diversas formas:
#Posición, Keywords, Valores por defecto, 
#Función que se le pasará una colección de argumentos (*args):Acepta nº arbitrario de args/ (**args):Acepta nº de args por nombre
#Los argumentos tras el * se convierten en keywprd-only

#VARIABLES. Lo ideal es declarar e inicializar siempre las variables
# En Python podemos asignar una variable a otra variable diferente.
var = "Hola mundo"
var2 = var
print(var2)

#CONTROL DE FLUJO
#If
a=10
b=3
if a>b:
    print('Si se cumple la condición')
    print('Ya estamos fuera del if')
#Else o elif (else if): Crea múltiples ramas condicionales
a = 10
b = 3
if a < b:
    print ('Se ha cumplido la condición')
else:
     print ('No se ha cumplido la condición')

     print ('Ya estamos fuera del if')
#Para evaluar más condiciones usamos elif
#OPERADOR TERNARIO: Es una sentencia en sí misma y no una sentencia (diferencia con el if)
a=10
b=3
resultado= 20 if a < b else 30
print(resultado)

#WHILE
a=0
while a<3:
    print(a, end=' ')
    a +=1
print(a)
print('Hemos salido fuera del while')

#Sentencias que permiten alterar el flujo de los bucles
#Break:Interrumpe el flujo
a=5
while a:
    print(a, end=' ')
    if a == 2:
        break
    a -=1
print('\nFuera del bucle.')
print('Valor de "a": {}'.format(a))

#CONTINUE, permite interrumpir la iteración actual
#PASS: Deja bucles vacíos

#Bucle FOR: la diferencia con while es que evalúa expresiones
a=0
for x in [1,2,3,4]:
    a +=x
    print (a)

for c in ['Me gusta Python!']:
    print (c, end=' ')
#Para lo que más se utiliza FOR es para recorrer diccionarios:
keys=['nombre','apellidos','edad']
values=['Guido','Van Rossum','60']
d=dict(zip(keys,values)) #Creamos el diccionario
for k in d:
    info='{}:{}'.format(k,d[k]) #str.format: sustituye las llaves de la cadena por los parámetros que le pasamos al llamarlo
    print(info)                 #k:clave del diccionario/d[k]:valor del diccionario correspondiente a dicha clave

#Tuplas: Se asemejan a una lista pero a diferencia de estas no pueden ser modificadas tras su creación
#Se utiliza mucho para bucles FOR
#Es útil para recorrer dos listas a la vez
a=[10,20,30,40]
b=[5,25,50,10]
for a,b in zip(a,b):
    m=max(a,b) #Devuelve el maximo entre a y b
    print(m, end=' ')
#Entrada de datos:
#RECIBIR INFO DEL USUARIO
#input
#nombre=input('Introduce tu nombre:')

#Pedir varios valores a la vez: map
#a,b,c= map(int,input("Introduzca los números: ").split())
#print("Los números son: ", end=" ")
#print(a,b,c)

#Para introducir elementos en las listas append() y en los conjuntos add()
#Salida de datos: print()
#Salida de datos con formato
#f o F
name = "Antonio"
print(f'Hola {name}! ¿Qué tal?')
#format() o con %