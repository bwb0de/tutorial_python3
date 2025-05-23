#
# Refatore o código
#

def input_cargo():
    cargo_informado = input().strip().capitalize()
    if cargo_informado == "Gerente": return "Gerente"
    elif cargo_informado == "Engenheiro": return "Engenheiro"
    else: return "Outros"
    

def avaliar_reajuste_por_tempo_servico():
    tempo_de_servico = int(input().strip())
    if tempo_de_servico > 6: return "Reajuste máximo"
    elif 3 < tempo_de_servico <= 6: return "Reajuste médio"
    else: return "Reajuste mínimo"


def avaliar_salario_informado(salario_minimo):
    salario_recebido = float(input())
    if salario_recebido < salario_minimo:
        return 0 #Salário inválido
    return salario_recebido

  
cargo = input_cargo()
reajuste_tempo_de_servico = avaliar_reajuste_por_tempo_servico()
salario_atual_valido = avaliar_salario_informado(1039.00)
reajuste = 0.0
salario_reajustado = 0.0

if not salario_atual_valido:
    print("Salário inválido!")
else:

    if cargo == "Gerente":
        if reajuste_tempo_de_servico == "Reajuste máximo":   reajuste = salario_atual_valido * 0.15
        elif reajuste_tempo_de_servico == "Reajuste médio":  reajuste = salario_atual_valido * 0.13
        elif reajuste_tempo_de_servico == "Reajuste mínimo": reajuste = salario_atual_valido * 0.12
    
    elif cargo == "Engenheiro":
        if reajuste_tempo_de_servico == "Reajuste máximo":   reajuste = salario_atual_valido * 0.14
        elif reajuste_tempo_de_servico == "Reajuste médio":  reajuste = salario_atual_valido * 0.11
        elif reajuste_tempo_de_servico == "Reajuste mínimo": reajuste = salario_atual_valido * 0.07
 
    else:
        reajuste = salario_atual_valido * 0.05

    print(f"{reajuste:.2f}")
    print(f"{salario_atual_valido+reajuste:.2f}")


