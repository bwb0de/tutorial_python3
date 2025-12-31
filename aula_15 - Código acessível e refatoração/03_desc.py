notebooks = int(input("Quantos notebooks comprou? "))
iPads = int(input("Quantos iPads comprou? "))
forma_pagamento = int(input("Qual a forma de pagamento? ([0] a vista; [1] a prazo "))

valor_notebooks = notebooks*1500
valor_iPads = iPads*1000

valor_total = valor_notebooks + valor_iPads
valor_ajustado_apos_pagamento = valor_total
valor_desconto_unidades = valor_ajustado_apos_pagamento


unidades = notebooks + iPads

if unidades >= 3:
    valor_desconto_unidades -= 500
    valor_ajustado_apos_pagamento -=500



if forma_pagamento == 0:
    valor_ajustado_apos_pagamento -= valor_ajustado_apos_pagamento*0.10
elif forma_pagamento == 1:
    valor_ajustado_apos_pagamento += valor_ajustado_apos_pagamento*0.08
else:
    print("Forma de pagamento desconhecida!")

print(f"Valor sem desconto: {valor_total:.2f}")
print(f"Valor com desconto [promoção unidades adquiridas]: {valor_desconto_unidades:.2f}")
print(f"Valor ajustado conforme o tipo de pagamento: {valor_ajustado_apos_pagamento:.2f}")
