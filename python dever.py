# # def conveterTemperatura(celsius):
# #     conversao = (celsius * 1.8 + 32)
# #     return conversao

# # celsius = int(input("Coloque um valor de temperatura em celsius: "))
# # resposta = conveterTemperatura(celsius)
# # print(f"Em Fahrenheit o valor é {resposta}! :D")


# # def calculadorFatorial(valor):
# #     if valor == 0:
# #         return 1
# #     else:
# #         fatorial = 1
# #         for numero in range(1, valor + 1):
# #             fatorial *= numero
# #         return fatorial
# # valor = int(input("Coloque um valor inteiro para fatoriar: "))
# # resposta = calculadorFatorial(valor)

# # print(f"{valor}! = {resposta} :D")

# # def perimetro(altura,base):
# #     calculo = 2 * (altura + base)
# #     return calculo
# # altura = float(input("Altura: "))
# # base = float(input("Base: "))

# # resposta = perimetro(altura,base)
# # print(f"O perimetro é {resposta}! :D")

# def calcular_media(media):
#     lista = [] 
#     if len(media) == 0:
#         return 0
#     else:
#         soma = sum(media) // len(media)
#         return soma
# valores = {float(numero) for numero in (input("Valores da lista: "))}
# armazem = calcular_media(valores)
# print(f"A média vale {armazem}! :D")

# def adicao(valor1,valor2):
#     adicao1 = valor1 + valor2
#     print(f"{valor1} + {valor2} = {adicao1}")
    
# def subtracao(valor1,valor2):
#     subtracao1 = valor1 - valor2
#     print(f"{valor1} - {valor2} = {subtracao1}")
    
# def multiplicacao(valor1,valor2):
#     multiplicacao1 =  valor1 * valor2
#     print(f"{valor1} x {valor2} = {multiplicacao1}")
    
# def divisao(valor1,valor2):
#     divisao1 =  valor1 / valor2
#     print(f"{valor1} ÷ {valor2} = {divisao1}")

# def exponenciacao(valor1,valor2):
#     exponenciacao1 = valor1 ** valor2
#     print(f"{valor1}^{valor2} = {exponenciacao1}")

# def fatorial(valor3):
#     if valor3 == 0:
#         return 1
#     elif valor3 != 0:
#         fatorial1 = 1
#         for numero in range(1, valor3 + 1):
#             fatorial1 *= numero
#         return fatorial1

# def pergunta():
#     while True:
#         pergunta1 = input("Deseja começar?(S/N): ")
#         if pergunta1 == "N" or pergunta1 == "n":
#             print('---- Poxa! volte sempre que puder :( ----')
#             break
#         else:
#             menu = '''
#             -------- CALCULADORA --------
#             ------  1 - adição (+) ------
#             ----- 2 - subtração (-) -----
#             --- 3 - multiplicação (X) ---
#             ------ 4 - divisão (÷) ------
#             --- 5 - exponenciação(^x) ---
#             ----- 6 - fatorial (!) ------
#             '''
#             print(menu)
#             pergunta2 = int(input("Insira aqui um dos números de cima: "))
#             if pergunta2 == 6:
#                 valor3 = int(input("Insira um valor aqui: "))
#                 resposta = fatorial(valor3)
#                 print(f"{valor3}! = {resposta}")
#             else:
#                 valor1 = int(input("Insira um valor aqui: "))
#                 valor2 = int(input("Insira, agora, um outro valor aqui: "))
#                 if pergunta2 == 1:
#                     adicao(valor1,valor2)
#                 elif pergunta2 == 2:
#                     subtracao(valor1,valor2)
#                 elif pergunta2 == 3:
#                     multiplicacao(valor1,valor2)
#                 elif pergunta2 == 4:
#                     divisao(valor1,valor2)
#                 elif pergunta2 == 5:
#                     exponenciacao(valor1,valor2)

# print("----Bem vinde a calculadora 2.0! :D----")
# pergunta()