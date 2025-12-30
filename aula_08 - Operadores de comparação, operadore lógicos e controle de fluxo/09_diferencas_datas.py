#
# Crie um programa que retorne a diferença em dias entre duas datas.
# As datas fornecidas deverão ser do mesmo ano.
# As datas fornecidas deverão ser válidas.
# Considere os anos bissextos.
#   - Um ano é bissexto se for divisível por 4 e não for divisível por 100
#   - Ou se for dicisível por 400

# Não utilize os módulos nativos do python!
#


data1 = input("Insira a 1ª data [##/##/####]: ").strip()
data2 = input("Insira a 2ª data [##/##/####]: ").strip()

dia1, mes1, ano1 = data1.split("/")
dia2, mes2, ano2 = data2.split("/")

dia1, mes1, ano1 = int(dia1), int(mes1), int(ano1)
dia2, mes2, ano2 = int(dia2), int(mes2), int(ano2)


#Avaliação ano bissexto
bissexto = False
if (ano1 % 4 == 0 and ano1 % 100 != 0) or (ano1 % 400 == 0): bissexto = True


#Validação
if ano1 != ano2:
	print("As datas precisam ter o mesmo ano...")
	exit()

if dia1 < 0 or dia2 < 0 or mes1 < 0 or mes2 < 0 or mes1 > 12 or mes2 > 12:
	print("Data inválida!")
	exit()

if mes1 in {1,3,5,7,8,10,12} and dia1 > 31:
	print("Data inválida!")
	exit()
elif not mes1 in {1,2,3,5,7,8,10,12} and dia1 > 30:
	print("Data inválida!")
	exit()


if mes2 in {1,3,5,7,8,10,12} and dia2 > 31:
	print("Data inválida!")
	exit()
elif not mes2 in {1,2,3,5,7,8,10,12} and dia2 > 30:
	print("Data inválida!")
	exit()


if bissexto and (mes1 == 2 and dia1 > 29):
	print("Data inválida!")
	exit()
elif not bissexto and (mes1 == 2 and dia1 > 28):
	print("Data inválida!")
	exit()

if bissexto and (mes2 == 2 and dia2 > 29):
	print("Data inválida!")
	exit()
elif not bissexto and (mes2 == 2 and dia2 > 28):
	print("Data inválida!")
	exit()



#Dias por mês
dias_jan = 31
if bissexto:
	dias_fev = 29
else:
	dias_fev = 28
dias_mar = 31
dias_abr = 30
dias_mai = 31
dias_jun = 30
dias_jul = 31
dias_ago = 31
dias_set = 30
dias_out = 31
dias_nov = 30
dias_dez = 31

meses_ano = [dias_jan, dias_fev, dias_mar, dias_abr, dias_mai, dias_jun, dias_jul, dias_ago, dias_set, dias_out, dias_nov, dias_dez]


#Calcula dia do ano conforme a data
dias_data1 = sum(meses_ano[:mes1-1]) + dia1
dias_data2 = sum(meses_ano[:mes2-1]) + dia2



#Compara os dias e calcula a diferença
if dias_data1 > dias_data2:
	print('A diferença em dias entre as datas é:', dias_data1 - dias_data2)
elif dias_data1 < dias_data2:
	print('A diferença em dias entre as datas é:', dias_data2 - dias_data1)
else:
	print('Mesma data')
