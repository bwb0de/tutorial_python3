mes, dia_semana_inicia = input().split()
mes, dia_semana_inicia = int(mes), int(dia_semana_inicia)

assert(1 <= mes <= 12)
assert(1 <= dia_semana_inicia <= 7)

total_dias = 0

if mes == 1: total_dias = 31
elif mes == 2: total_dias = 28
elif mes == 3: total_dias = 31
elif mes == 4: total_dias = 30
elif mes == 5: total_dias = 31
elif mes == 6: total_dias = 30
elif mes == 7: total_dias = 31
elif mes == 8: total_dias = 31
elif mes == 9: total_dias = 30
elif mes == 10: total_dias = 31
elif mes == 11: total_dias = 30
elif mes == 12: total_dias = 31

total_dias -= 7 - (dia_semana_inicia - 1)
semanas = 1

semanas += (total_dias // 7)

if total_dias % 7 > 0:
    semanas += 1

print(semanas)
