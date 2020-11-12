import re
cadena = input("ingresa el texto: ")
print("el texto es: "+cadena)

print("ingresa un una opcion")
print("1: cantidad de vocales")
print("2: cantidad de palabras")
print("3: cantidad de numeros")
print("4: cantidad de palabras que inicien con mayuscula")
print("5: cantidad de palabras que no finalizen con vocal")
numero = int(input())
cont=0


if numero==1:
	#cantidad de vocales
	patron = re.compile('[aeiouAEIOU]')
	for match in re.finditer(patron, cadena):
		cont=cont+1


if numero==2:
	#cantidad de palabras
	patron = re.compile('[a-zA-Z]+[a-zA-Z]')
	for match in re.finditer(patron, cadena):
		cont=cont+1


if numero==3:
	#cantidad de numeros
	patron = re.compile('\d{1,10}')
	for match in re.finditer(patron, cadena):
		cont=cont+1


if numero==4:
	#cantidad de palabras que inicien con mayuscula
	patron = re.compile('[A-Z]\w+')
	for match in re.finditer(patron, cadena):
		cont=cont+1


if numero==5:
	#cantidad de palabras que inicien con mayuscula
	patron = re.compile('[a-zA-Z0-9]+[^aeiou]\s')
	for match in re.finditer(patron, cadena):
		cont=cont+1


print(cont)