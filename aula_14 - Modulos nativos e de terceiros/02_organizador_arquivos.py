#
# Crie um script que organize os arquivos de uma pasta alvo separando-os
# por tipo nas subpastas: Músicas, Vídeos e Documentos
#
# Dicas: use os módulos sys (para capturar argumentos da linha de 
# comando), os (para listar o conteúdo de pastas) e shutil (para 
# realizar as operações de movimentação dos arquivos), explore estes
# módulos pelo shell interativo ou pela documentação on-line.
#

import sys
import os
import shutil

args = sys.argv[1:]

if len(args) < 1:
	print("É necessário indicar um 'diretório alvo'.")
	exit(1)

elif len(args) > 1:
	print("Apenas o argumento 'diretorio alvo' deve ser fornecido.")
	exit(1)

DIRETORIO_ALVO = args[0]
DIRETORIO_INICIO = os.getcwd()
SHELL_CMD = shutil.move

os.chdir(DIRETORIO_ALVO)

arquivos = os.listdir('.')

try: os.mkdir("Músicas")
except FileExistsError: pass

try: os.mkdir("Videos")
except FileExistsError: pass

try: os.mkdir("Documentos")
except FileExistsError: pass

for arquivo in arquivos:
	if any([
		arquivo.endswith('.mp3'),
		arquivo.endswith('.ogg'),
		arquivo.endswith('.wav'),
	]):
		SHELL_CMD(arquivo, f".{os.sep}Músicas{os.sep}{arquivo}")
	elif any([
		arquivo.endswith('.odf'),
		arquivo.endswith('.doc'),
		arquivo.endswith('.docx'),
	]):
		SHELL_CMD(arquivo, f".{os.sep}Documentos{os.sep}{arquivo}")
	elif any([
		arquivo.endswith('.avi'),
		arquivo.endswith('.mpeg'),
		arquivo.endswith('.mov'),
	]):
		SHELL_CMD(arquivo, f".{os.sep}Videos{os.sep}{arquivo}")

