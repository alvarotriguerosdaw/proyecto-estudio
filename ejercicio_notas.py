#Tienes que crear un programa que reciba los datos de un alumno, calcule su nota media, determine su estado académico y diga si puede compensar.


def calcular_media (nota1, nota2, nota3):
    if (nota1 > 10 or nota2 > 10 or nota3 > 10):
        print(f"Una de las nota no es valida")
    elif (nota1 < 0 or nota2 < 0 or nota3 < 0):
        print(f"Una de las nota no es valida")
    else:
        media = (nota1 + nota2 + nota3)/3
        return media 


def obtener_estado (media):
    if (media >= 9): 
        return "Sobresaliente"
    elif(media < 9 and media >= 7):
        return "Notable"
    elif(media < 7 and media >= 5):
        return "Aprobado"
    else:
        return "Suspenso"

# print(f"{obtener_estado(1)}")
# print(f"{obtener_estado(7)}")
# print(f"{obtener_estado(6)}")
# print(f"{obtener_estado(4)}")
# print(f"{obtener_estado(9)}")

def puede_compensar(media):
    if(media >=4.5):
        return True
    else:
        return False

# print(F"{puede_compensar(4.6)}")
# print(F"{puede_compensar(4.5)}")
# print(F"{puede_compensar(4.4)}")

def mostrar_resultado(alumno, nota1, nota2, nota3):
    print(f"Alumno: {alumno}")
    nota_media  = calcular_media(nota1,nota2,nota3)
    estado_media = obtener_estado(nota_media)
    print(f"Media: {nota_media}")
    print(f"Estado: {estado_media}")
    recupera = puede_compensar(nota_media)
    if (recupera):
        print(f"Puede compensar")
    else:
        print(f"No puede compensar")

mostrar_resultado("gochi", 10, 5, 0)
mostrar_resultado("julia", 10, 10, 9.9)
mostrar_resultado("David", 1, 4, 3)