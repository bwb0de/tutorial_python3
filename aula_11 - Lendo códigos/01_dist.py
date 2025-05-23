f = open('p.txt', 'r')
lp = f.read().split()
t = len(lp)
f.close()

ldist = [
	['Jussara'],
	['Antônio'],
	['Silvana']
]
	
for i, p in enumerate(lp):
	dist_i = i % 3
	ldist[dist_i].append(p)

for subl in ldist:
	pessoa = subl[0]
	procs = subl[1:]
	procs_n = len(procs)
	print(f'{pessoa} [{procs_n}]:')
	for p in procs:
		 print(f'  - {p}')
	print('\n')

print(f'Total processos: {t}')

