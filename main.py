from src.Dado import Dado

cor  = input("Cor do Dado:")
qtde = int(input("Quantidade de Lados:"))

dado = Dado(cor, qtde)

dado.setCor(cor)
dado.setLado(qtde)

print("Cor do Dado:", Dado.getCor(dado))
print("Lado do Dado:", Dado.getLado(dado))

while True:
    rodar = input("Rodar o dado novamente?<S/n>\n:")
    if rodar == "S" or cond == "s":
        dado.setLado(qtde)
        print("Lado do Dado:", Dado.getLado(dado))
    else:
        break
