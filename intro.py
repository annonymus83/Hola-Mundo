print("Hola Mundo")

# variables
nombre_curso = "Ultimate Python"
nombre1 = "Mundo"
print(nombre_curso, nombre1)
alumnos = 5000
punaje = 9.9
publicado = True 

#strings
nombreCurso = "Ultimate python"
descripcion = """ 
Ultimate python,
este curso contempla todos los detalles 
que necesitas aprender para encontrar
 trabajo como programador
"""

print(len(nombreCurso))
print(nombreCurso[0])
print(nombreCurso[0:8])

nombre = "Nicolas"
apellido = "Schurmann"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

numero = 2
#numero = numero + 2 
numero += 2
print("numero", numero) #esto me devuelve 4

#Calculadora

n1 = input("ingresa primer numero") #al ejecutar esto en la terminal me dira que le de un nro
n2 = input("ingresa primer numero")

# print(n1 + n2) esto no devuelve la suma de n1 y n2 sino su concatenacion

n1 = int(n1)
n2 = int(n2)
print(n1 + n2) #Ahora si

#otro ejemplo
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la multiplicacion es {multi}.
el resultado de la division es {div}.
"""

print(mensaje)

#tipos

print(bool("")) # = false
print(bool("0")) # true
print(bool(None)) # = false
print(bool(" ")) # = true
print(bool(0)) # = false


# sentencias condicionales
edad = 60
if edad > 17:
    print("puede ver la pelicula")
elif edad > 54:
    print("puede ver la peli con descuento")
else:
    print("no puedes entrar")

print("Listo")

# operador ternario


mensage = "Es mayor" if edad > 17 else "es menor"
# edad = 15
# if edad > 17:
#     mensage = "es mayor" 
# else:
#     mensage = "es menor"

print(mensage)

#operadores logicos 

gas = True
encendido = True
edad1 = 18

if gas and encendido:
    print("Puedes avanzar")

#otro ejplo
if not gas and (encendido or edad > 17):
    print("Puedes avanzar")


# cadena de comparadores 
if edad >= 15 and edad <= 65:
    print("puede entrar a la piscina")

# otro caso
if 15 <= edad <= 65:
    print("puede entrar a la piscina")

#iteracion

for numero in range(5):
    print(numero)

buscar = 3

# for numeros in range(5):
#     print(numeros)
#     if numeros == buscar:
#         print("encontrado", buscar)
#         break
# else:
#     print("no encontre nro buscado :(")

for char in "Ultimate python":
    print(char)


while numero < 100:
    print(numero)
    numero *= 2

for j in range(3):
    for k in range(2):
        print(f"{j}, {k}")

#Funciones

def hola():
    print("Hola Mundo")
    print("Ultimate python")

hola()

#Funciones con parametros y argumentos
def holas(nombreDeUs):
    print("Hola Mundo")
    print(f"Bienvenido {nombreDeUs}")

holas("Chanchito Feliz")
            

def hola1(Nombre, Apellido="Feliz"):
    print("Hola Mundo")
    print(f"Bienvenido {Nombre} {Apellido}" )

hola1("nico", "Schurmann")
hola1("Chanchito")

# xars
# def sumas(*numeros):
#     resultado = 0
#     for numero in numeros:
#         resultado += numero
#     print(resultado)

# sumas(2,5,7)
# sumas(2,5)
# sumas(2,8,7,45,32)

#Return
def suma(a, b):
    res = a + b
    return res

c = suma(1, 2)
d = suma(c, 2)

print(d)



