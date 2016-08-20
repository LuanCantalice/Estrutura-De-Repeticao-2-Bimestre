populacaoA = 80000
populacaoB = 200000
anos = 0
crescimentoA = 0.03
crescimentoB = 0.015

while (populacaoA < populacaoB):
    anos = anos + 1
    populacaoA = populacaoA + (populacaoA * crescimentoA)
    populacaoB = populacaoB + (populacaoB * crescimentoB)
print("Após", anos, "anos o país A ultrapassou o país B em número de habitantes.")
	
