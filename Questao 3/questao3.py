nome = input(" Digite seu nome: ")
while ( len(nome) < 3):
	print(" Nome inválido! (Tem menos que 3 caracteres) ")
	nome = input(" Digite seu nome: ")

idade = eval(input(" Digite sua idade: "))
while (idade > 150 or idade < 0):
	print(" Idade inválida! (É maior que 150 ou menor que 0) ")
	idade = eval(input(" Digite sua idade: "))

salario = eval(input(" Digite seu salário: "))
while (salario < 0):
	print(" Salário Inválido! (É menor que zero) ")
	salario = eval(input(" Digite seu salário: "))

sexo =  input(" Digite seu sexo (f para feminino ou m para masculino) ")
while (sexo != "f" and sexo != "m"):
	print(" Sexo inválido! (Ele deve ser 'f' ou 'm') ")
	sexo =  input(" Digite seu sexo (f para feminino ou m para masculino) ")

estadoCivil = input(" Digite seu estado civil (s, c, v, d) : ")
while (estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd'):
	print( " Estado civil inválido! (Ele deve ser 's', 'c', 'v' ou 'd' ")
	estadoCivil = input(" Digite seu estado civil (s, c, v, d) : ")

print(" Seu nome é", nome,"sua idade é", idade,"seu salário é", salario,"você é do sexo", sexo,"e seu estado civil é", estadoCivil)
	
