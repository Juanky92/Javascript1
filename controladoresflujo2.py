#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Programa que lea números desde el teclado hasta que se 
#introduzca un número negativo. Cuando eso ocurra mostrará
#la cantidad de números introducidos y es la suma de los mismos

suma=0#Se debe inicializar una variable para los bucles
cuenta=0#Se debe inicializar una variable para los bucles
numero= int(raw_input('Haz el favor de meter un número: '))
while numero>=0:
	suma = suma + numero
	cuenta= cuenta +1
	numero= int(raw_input('Haz el favor de meter un número: '))#declaro otro numero para poder terminar el bucle
																#sino se convertiria en un bucle infinito
print cuenta
print suma

li=['urrrrllll','Jaime',123,165,True]#lista
for elemento in li:#Para cada elemento de la lista
	print elemento# Muestra los elemento que componen la lista

nus=[1,2,3,4,45,456,543,78]#lista
suma=0#Inicializar la variable suma
for elemento in nus:#por cada elemento en la lista
	suma=suma+elemento#Sumar los elementos de una lista
print suma#muestra la suma

nus=[1,2,3,4,45,456,543,78]#lista
suma=0#Inicializar la variable suma
for elemento in nus:#por cada elemento en la lista
	suma+=elemento#Sumar los elementos de una lista de forma mas simplificada
print suma#muestra la suma
	
