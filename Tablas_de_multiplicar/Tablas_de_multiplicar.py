import sys
print("python version:" + sys.version)

numero = 4
limite = 10

for i in range(limite + 1):
	valor = numero * i
	print(f" {numero}    X    {i}  =  {valor} ") 


with open(f"tabla del numero {numero}.txt", 'w') as file:

	for i in range(limite + 1):
		valor = numero * i
		file.write(f" {numero}    X    {i}  =  {valor} \n")

	file.write(f"\n Esta es la tabla de multiplicar del numero: {numero}\n ")
file.close()
print(f"tabla del {numero} creada")
