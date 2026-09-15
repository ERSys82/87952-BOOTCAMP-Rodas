# * int
numero = 10
#print(f"La variable numero tiene un {numero}  y es de tipo {type(numero)}")
print(f"La variable numero tiene un {numero}  y es de tipo {type(numero).__name__}")

# * str
nombre = "Eduardo"
#print(f"La variable numero tiene un {numero}  y es de tipo {type(numero)}")
print(f"La variable nombre tiene un {nombre}  y es de tipo {type(nombre).__name__}")

# * bool
condicion = True
print(f"La variable condicion tiene un {condicion} y es de tipo {type(condicion).__name__}")

# * float
numero_con_coma = 15.5
print(f"La variable numero_con_coma tiene un {numero_con_coma} y es de tipo {type(numero_con_coma).__name__}")

# * complex
complejo = 1 + 2j
print(f"La variable complejo tiene un {complejo} y es de tipo {type(complejo).__name__}")

# * None
vacia = None
print(f"La variable vacia tiene un {vacia} y es de tipo {type(vacia).__name__}")

#------------------------------------------------------------------------------------------
#  * Listas (se pueden modificar)
lista = [1,2,3,4,5,6]
# Las listas se pueden modificar por ejemplo...
lista.append(7)
lista = lista + [8]
print(f"La variable lista tiene un {lista} y es de tipo {type(lista).__name__}")

#  * Tuplas, Son como las listas pero no se pueden modificar
tupla = (1,2,3,4,5)
print(f"La variable tupla tiene un {tupla} y es de tipo {type(tupla).__name__}")
tupla_un_elemento = (6,)
print(f"La variable tupla_un_elemento tiene un {tupla_un_elemento} y es de tipo {type(tupla_un_elemento).__name__}")

#  * Diccionarios (Como un jsson)
persona = {
    "nombre" : "Juan",
    "apellido" : "Perez",
    "edad" : 25
}
print(f"La variable persona tiene un {persona} y es de tipo {type(persona).__name__}")

# Uso de los tres en uno:
tupla_claves = ('a', 'b', 'c')
lista_valores = [1, 2, 3]
# Generar el diccionario
resultado = dict(zip(tupla_claves, lista_valores))
print(resultado)

#  * set
pares_del_1_al_10 = {2,4,6,8,10}
print(f"La variable pares_del_1_al_10 tiene un {pares_del_1_al_10} y es de tipo {type(pares_del_1_al_10).__name__}");
if 2 in pares_del_1_al_10:
    print("El numero 2 esta en el set")

#  * range
rango = range(1,11)
print(f"La variable rango tiene un {rango} y es de tipo {type(rango).__name__}")

#  * range
#Defino un rango del 1 al 10
rango = range(1,11)
print(f"La variable rango tiene un {rango} y es de tipo {type(rango).__name__}")
for numero in rango:
    print(numero)

#Ejemplo si queiro iterar los nuermos de 2 en 2
print("------------------------")
for numero in range(1,11,2):
  print(numero)

#Recorrer strings
print("------------------------------------")
cadena = "Hola"

for letra in cadena:
    print(letra)
print("------------------------------------")
lista = [1,2,3,4,5,6]
for numero in lista:
    print(numero)

#-----------------------------------------------------------------
def sumar(a,b):
    return a + b

cuatro = sumar(2,2)
print(f"La suma es {cuatro}")
print(type(sumar))

#-----------------------------------------------------------------
# 1. Declaración del diccionario del personaje
personaje = {
    "nombre": "Eldrin el Sabio",
    "clase": "Mago",
    "nivel": 12,
    "puntos_vida": 85,
    "habilidades": ["Bola de fuego", "Teletransportación", "Escudo arcano"],
    "inventario": {"oro": 450, "pociones": 3, "baston": 1}
}

# 2. Recorrido del diccionario con un bucle for
print("--- Recorriendo el diccionario ---")
for clave, valor in personaje.items():
    print(f"{clave.capitalize()}: {valor}")

#-----------------------------------------------------------------
from chronos import Chronos2Pipeline

pipeline = Chronos2Pipeline.from_pretrained("amazon/chronos-2")

#-----------------------------------------------------------------
import numpy as np

datos = np.array([1,2,3,4,5,6,7,8,9], dtype=np.float32)

prediccion  = pipeline.predict([datos], prediction_length=1)

print(prediccion[0].mean())