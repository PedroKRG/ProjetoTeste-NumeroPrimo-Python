def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    print("Coloque um número para verificar se é primo:") 
    a = int(input())
    if eh_primo(a):
        print(a, 'é primo')
    else:
        print(a, 'não é primo')

if __name__ == "__main__":
    main()
