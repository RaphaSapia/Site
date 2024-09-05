print("Olá, Bemvindo a sua cauculadora financeira.")
print("Hoje vamos te ajudas a caucular seu investimento rumo a sua aposentaria.")

nome= input("Qual o seu nome?: ")

idade= int(input(f"Qual a sua idade {nome}: ?"))

invest_inicial= float(input("Quanto você deseja investir de início?: "))

invest_time= int(input("Por quantos meses você deseja investir?: "))

taxa= float(input("Qual a taxa mensal de retorno?: "))

aprote= float(input("Quanto você pretende investir por mês?: "))

renda_desejada= float(input("Quanto você deseja receber por mês em sua aposentadoria?: "))

tempo_decorrido= 0
while tempo_decorrido < invest_time:
    if tempo_decorrido == 0:
       montante= invest_inicial * (1 + taxa) ** 1
       montante= round(montante,2)
       tempo_decorrido = tempo_decorrido + 1

    else:
       montante= (montante + aprote) * (1 + taxa)** 1
       montante= round(montante,2)
       tempo_decorrido = tempo_decorrido + 1

print("--------------------------------------------------------------------")



print(f"No fim do período de investimento você terá R$ {montante}!")

renda_mensalfinal = (montante * taxa)
renda_mensalfinal = round(renda_mensalfinal,2)

if renda_mensalfinal >= renda_desejada:
    print(f"Parabéns, seu salário mensal será de R$: {renda_mensalfinal} ")

elif renda_mensalfinal < renda_desejada:
    print(f"Infelizmente com este investimento, o salário desejado será de R$: {renda_mensalfinal}, menor do que o desejado.")

