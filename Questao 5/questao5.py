populacaoA = eval(input(" Digite a população de A: "))
populacaoB = eval(input(" Digite a população de B: "))
anos = 0
crescimentoA = eval(input(" Digite a porcentagem de crescimento de A: "))
crescimentoB = eval(input(" Digite a porcentagem de crescimento de B: "))
porcentagemA = (crescimentoA/100)
porcentagemB = (crescimentoB/100)

while (populacaoA < populacaoB):
    anos = anos + 1
    populacaoA = populacaoA + (populacaoA * porcentagemA)
    populacaoB = populacaoB + (populacaoB * porcentagemB)
print("Após", anos, "anos o país A ultrapassou o país B em número de habitantes.")
	
