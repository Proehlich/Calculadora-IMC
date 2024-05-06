n1 = float(input('\033[33mDigite seu PESO: (KG) '))
n2 = float(input('\033[33mDigite sua ALTURA: (M) '))
imc = n1 / (n2 ** 2)
print('\033[34mSeu IMC é {:.2f}'.format(imc))
if imc <= 18.5 :
    print('\033[33mVocê está abaixo do peso IDEAL!')
elif 18.5 <= imc < 25:
    print('\033[32mVocê está no peso IDEAL!')
elif 25 <= imc < 30:
    print('\033[33mVocê está com SOBREPESO!')
elif 30 <= imc < 40:
    print('\033[35mVocê está em OBESIDADE!')
elif imc >= 40:
    print('\033[31mVocê está em OBESIDADE MORBIDA!')
