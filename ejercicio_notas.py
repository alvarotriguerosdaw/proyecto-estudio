#Tienes que crear un programa que reciba los datos de un alumno, calcule su nota media, determine su estado académico y diga si puede compensar.

alumno = "Alvaro"

def calcular_media (nota1, nota2, nota3):
    if (nota1 > 10 or nota2 > 10 or nota3 > 10):
        print(f"Una de las nota no es valida")
    elif (nota1 < 0 or nota2 < 0 or nota3 < 0):
        print(f"Una de las nota no es valida")
    else:
        media = (nota1 + nota2 + nota3)/3
        return media 

calcular_media(11,7,6)

def obtener_estado (media):
    if (media >= 9):
        media = "Sobresaliente"
        return media
    elif(media < 9 and media >= 7):
        media = "Notable"
        return media
    elif(media < 7 and media >= 5):
        media = "Aprobado"
        return media
    else:
        media = "Suspenso"
        return media




