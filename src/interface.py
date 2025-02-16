from src.calculadora import Calculadora

def main():
    calc = Calculadora()
    
    print("Calculadora Básica")
    print("Escolha a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    try:
        opcao = int(input("Digite o número da operação desejada: "))
        if opcao not in [1, 2, 3, 4]:
            print("Opção inválida!")
            return
        
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        
        if opcao == 1:
            print("Resultado:", calc.somar(a, b))
        elif opcao == 2:
            print("Resultado:", calc.subtrair(a, b))
        elif opcao == 3:
            print("Resultado:", calc.multiplicar(a, b))
        elif opcao == 4:
            print("Resultado:", calc.dividir(a, b))
    
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de inserir números válidos.")

if __name__ == "__main__":
    main()