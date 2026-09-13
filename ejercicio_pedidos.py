# Ejercicio Pedidos

def calcular_subtotal(precio, cantidad):
    if (precio <= 0):
        print(f"El precio no puede ser 0 o negativo")
        return
    elif (cantidad <= 0):
        print(f"La cantidad no puede ser 0 o negativo")
        return
    else:
        subtotal = precio * cantidad
        return subtotal

# print(f"{calcular_subtotal(10, 5)}")

def calcular_descuento(subtotal, vip):
    if(vip):
        print(f"Has recibido un descuento de 15% por ser VIP")
        return round(subtotal/1.15,2)
    else:
        return subtotal

# print(f"{calcular_descuento(100, False)}")    

def calcular_envio(subtotal):
    if(subtotal < 50):
        print(f"Tienes que pagar 4.99 de envio")
        return subtotal + 4.99
    else:
        return subtotal

# print(f"{calcular_envio(50.01)}")    

 
def mostrar_pedido(precio, cantidad, vip):
    subtotal  = calcular_subtotal(precio, cantidad)

    if(subtotal is None):
        return
        
    print(f"Precio:{precio}")
    print(f"Cantidad:{cantidad}")
    print(f"Subtotal:{subtotal}")
    subtotal = calcular_descuento(subtotal, vip)
    print(f"Subtotal:{subtotal}")
    subtotal = calcular_envio(subtotal)
    print(f"Precio final:{subtotal}")

mostrar_pedido(2, 1, False)
 