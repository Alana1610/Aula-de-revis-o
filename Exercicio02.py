
while True:
    numero= int(input("digite um numero:"))
    if numero >0 and numero %2 ==0:
        print(f"O numero é positivo e par")
    elif numero >0 and numero %2 ==0 :
        print(f"O numero é negativo e par")
    elif numero <0 and numero %2 ==0 :
        print(f"O numero é positivo e impar")
    else:
        print(f"O numero é negativo e impar")
        continuar= input("Deseja tentar com um novo numero?(s/n):").lower()
        if continuar != 's':
            print(f"Encerrando o programa")
            break