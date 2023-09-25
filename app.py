import datetime
#con base a la fecha actual obtener el año que el usuario cumplira 100
def calcular_fecha_cumple_100(nombre, edad):
    fecha_actual = datetime.datetime.now().year
    fecha_cumple_100 = fecha_actual + (100 - edad)
    mensaje = "Hola, {}! Cumplirás 100 años en el año {}.".format(nombre, fecha_cumple_100)
    return mensaje

#registro de los datos (nombre y edad)
def obtener_datos():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    return nombre, edad

#configuracion de la variable mensaje para obtener los datos de las demas funciones
def imprimir_mensaje_personalizado():
    nombre, edad = obtener_datos()
    mensaje = calcular_fecha_cumple_100(nombre, edad)
    print(mensaje)

imprimir_mensaje_personalizado()
