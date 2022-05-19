#Practica 6, Calculadora
#Axel Elian Amavizca Galaviz

#4 Operaciones basicas

#variable global

#r=0
#n1=0
#n2=0

def suma(n1,n2):
    print("La suma de 2 numeros")
    print("La suma de " + str(n1) + " + " + " " +str(n2) + " es igual a: ")
    r=n1+n2
    print("" + str(r))

def resta(n1,n2):
    print("La resta de 2 numeros")
    print("La resta de " + str(n1) + " - " + " " +str(n2) + " es igual a: ")
    r=n1-n2
    print("" + str(r))

def mult(n1,n2):
    print("La multiplicacion de 2 numeros")
    print("La multiplicacion de " + str(n1) + " X " + " " +str(n2) + " es igual a: ")
    r=n1*n2
    print("" + str(r))

def div(n1,n2):
    print("La division de 2 numeros")
    print("La division de " + str(n1) + " / " + " " +str(n2) + " es igual a: ")
    r=n1/n2
    print("" + str(r))

#def resta(n3):
    #print("La resta")
    #r2=r-n3
    #print("La resta  es = " + str(r2))


suma(1,2)
resta(4,2)
mult(2,2)
div(1,2)
