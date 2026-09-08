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

def saludar(nombre):
    return nombre

def apellidos(apellido1, apellido2):
    return (f"{apellido1} {apellido2}")

def nombre_completo(nombre, apellido1, apellido2):
        print(f"Hola {saludar(nombre)} {apellidos(apellido1, apellido2)}")

nombre = saludar("Alvaro")
dos_apellidos = apellidos("Trigueros","Vazquez")
nombre_completo("Alvaro" , "Trigueros" , "Vazquez")

def multiplicar(num1,num2):
    return num1 * num2

resultado = multiplicar(4,5)
print(f"El resultado es: {resultado}")

print(f"Ejercicio: precio final de una compra")

def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal

def descuento(subtotal):
    if subtotal >= 100:
        return 20
    elif subtotal >=50:
           return 10
    else:
        return 0 

# print(f"{descuento(120)}")
# print(f"{descuento(70)}")
# print(f"{descuento(30)}")
def mostrar_compra(precio, cantidad):
    print(f"Precio: {precio}")
    print(f"Cantidad: {cantidad}")
    subtotal = calcular_subtotal(precio, cantidad)
    print(f"Subtotal: {subtotal}")
    cantidad_descuento = descuento(subtotal)
    print(f"Descuento: {cantidad_descuento}")
    def calcular_precio(subtotal,descuento):
        precio_final = subtotal - descuento
        return precio_final
    
    print(f"Precio final: {calcular_precio(subtotal, cantidad_descuento)}")

mostrar_compra(10,0)





