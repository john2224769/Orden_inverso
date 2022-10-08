# Programa para invertir el orden de un numero de cuatro cifras

from turtle import st

#input
n = input("Ingrese un numero de cuatro cifras a invertir ")
n= int(n)
print(" ")

#processing
mod1=n%10
mod2=int((n%100)/10)
mod3=int((n%1000)/100)
mod4=int((n-(n%1000))/1000)

#output
print("El nuemro invertido es: "+str(mod1)+str(mod2)+str(mod3)+str(mod4))
