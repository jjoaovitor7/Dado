from src.Dado import Dado

def main():
    cor = str(input("Cor do Dado: "))

    try:
        qtde = int(input("Quantidade de Lados: "))
    except ValueError:
        print("Somente números.")
        return 0

    dado = Dado(cor, qtde)

    dado.setCor(cor)
    print("Cor do Dado:", Dado.getCor(dado))

    dado.rolar(qtde)
    print("Lado do Dado:", Dado.getLado(dado))

    while True:
        rolar = input("Rolar o dado novamente?<S/n>\n:")
        if rolar == "S" or rolar == "s":
            dado.rolar(qtde)
            print("Lado do Dado:", Dado.getLado(dado))
        else:
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrompido.")
