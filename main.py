from src.Dado import Dado

cor  = input("Cor do Dado:")
qtde = int(input("Quantidade de Lados:"))

dado = Dado(cor, qtde)

dado.setCor(cor)
dado.setLado(qtde)

print("Cor do Dado:", Dado.getCor(dado))
print("Lado do Dado", Dado.getLado(dado))
