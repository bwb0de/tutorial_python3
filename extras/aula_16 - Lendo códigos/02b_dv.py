n = int(input("Informe o número: "))

for cdt in range(n):
    cdt += 1
    if n % cdt == 0:
        print(cdt)
