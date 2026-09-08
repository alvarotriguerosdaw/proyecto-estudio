asignatura = "Programación"
minutos = 29
completada = True

print(asignatura)
print(minutos)
print(completada)

tipoAsignatura = type(asignatura)

print(tipoAsignatura)
print(type(minutos))
print(type(completada))

if minutos >=60:
    print("Sesión larga")
elif minutos >= 30:
    print("Sesion normal")
else:
       print("Sesión corta")

def mostrar_bienvenida():
    print("Bienvenidos al curso de Python")

mostrar_bienvenida()

# def saludar(nombre):
#     print(f"Hola {nombre}")

# def apellidos(apellido1, apellido2):
#     print(f" {apellido1} {apellido2}")

# def nombre_completo():
#     print(saludar() + apellidos())

# saludar("Alvaro")
# apellidos("Trigueros","Vazquez")
# nombre_completo()

def multiplicar(num1,num2):
    return num1 * num2

resultado = multiplicar(4,5)
print(f"El resultado es: {resultado}")