# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("\nSelecione o número da operação")

print("\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

a = input("\nDigite sua opção (1/2/3/4): ")

b = int(input('\nDigite o primeiro número: '))

c = int(input('\nDigite o segundo número: '))

if a > "4":
	print ("OPÇÃO INVALIDA")
elif a == "1":
	print("\n O resultado foi de: ", b + c)
elif a == "2":
	print("\n O resultado foi de: ", b - c)
elif a == "3":
	print("\n O resultado foi de: ", b*c)
elif a == "4" and c != 0 :
	print ("\n O resultado foi de: ", b/c)
else:
	print("\nO segundo número deve ser diferente de 0 para essa operação")
