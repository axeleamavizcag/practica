#Practica 5
#Manejo de métodos
#AXEL ELIAN AMAVIZCA GALAVIZ

#Manipulacion de las luces exteriores y interiores en una casa, en un ciclo de 60 segundos

# 4 tiempos (15min)
# 4 tonos
# 2 colores

#tigger

#Declaracion de variables



varlapso = 15

VCI = "#F7FF87"
VCF = "#FFF"

VT1 = .25
VT2 = .5
VT3 = .75
VT4 = 1


def inicio():
    etapa1()

def finalizar():
    print("Luces encendidas a todo color.")

def timer(minutos):
    print("Inicio conteo de 15" + str(minutos))
    #1000 falta funcion que cuente los 15 minutos
    print("Finalizado conteo de 15")

def luces(tono, color): 
    print("Se establece el color y tono")
    print("Color establecido: " + color)
    print("Tono establecido: " + str(tono))

def etapa1():
    print("Etapa uno iniciada")
    timer(varlapso)
    luces(VT1,VCI)
    print("Etapa uno finalizada")
    etapa2()

def etapa2():
    print("Etapa dos iniciada")
    timer(varlapso)
    luces(VT2,VCI)
    print("Etapa dos finalizada")
    etapa3()

def etapa3():
    print("Etapa tres iniciada")
    timer(varlapso)
    luces(VT3,VCF)
    print("Etapa tres finalizada")
    etapa4()

def etapa4():
    print("Etapa cuatro iniciada")
    timer(varlapso)
    luces(VT4,VCF)
    print("Etapa cuatro finalizada")
    finalizar()

print("Inicio de la manipulación de luces")

inicio()
    