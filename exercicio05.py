peso= float(input("Digite seu peso (em kg):"))
altura= float(input("Digite sua altura(em metros):"))
imc=peso/(altura**2)
print(f"seu imc é {imc:.2f}")
if imc <18.6:
    print("condição: abaixo do peso")
elif imc <25:
    print("Condição:peso ideal (parabens)")
elif imc<30:
    print("Condição:levemente acima do peso")
elif imc <35:
    print("Condição:Obsidade grau I")
elif imc <40:
    print("Condição: Obsidade grau II(severa)")
else:
    print("Condição:Obsidade grau III (mórbida)")
