nota = eval(input(" Digite a nota (0 a 10) : "))	
while (nota > 10 or nota < 0):
	print(" Nota inválida! (Ela é maior que 10 ou menor que 0) Por favor, digite novamente. ")
	nota = int(input(" Digite a nota (0 a 10) : "))
