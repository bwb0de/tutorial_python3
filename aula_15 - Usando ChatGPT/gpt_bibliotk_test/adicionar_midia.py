import sqlite3

def conectar():
    return sqlite3.connect("midias.db")

def listar_opcoes(cursor, tabela):
    cursor.execute(f"SELECT id, nome FROM {tabela}")
    opcoes = cursor.fetchall()
    for id_, nome in opcoes:
        print(f"{id_}: {nome}")
    return opcoes

def escolher_ou_adicionar(cursor, conexao, tabela, nome_campo):
    opcoes = listar_opcoes(cursor, tabela)
    escolha = input(f"Escolha um {nome_campo} pelo número ou digite um novo nome: ").strip()

    if escolha.isdigit() and int(escolha) in [id_ for id_, _ in opcoes]:
        return int(escolha)

    cursor.execute(f"INSERT INTO {tabela} (nome) VALUES (?)", (escolha,))
    conexao.commit()
    return cursor.lastrowid


def escolher_temas(cursor, conexao):
    temas_selecionados = set()
    
    while True:
        listar_opcoes(cursor, "tema")
        escolha = input("Escolha um ou mais temas pelo número (separados por vírgula), digite um novo tema ou pressione Enter para continuar: ").strip()
        
        if not escolha:
            break

        if all(part.strip().isdigit() for part in escolha.split(",")):  
            # Usuário escolheu números
            ids = {int(part.strip()) for part in escolha.split(",")}
            temas_selecionados.update(ids)
        else:
            # Usuário digitou um novo tema
            cursor.execute("INSERT INTO tema (nome) VALUES (?)", (escolha,))
            conexao.commit()
            temas_selecionados.add(cursor.lastrowid)

    return temas_selecionados


def adicionar_midia():
    conexao = conectar()
    cursor = conexao.cursor()

    titulo = input("Título: ").strip()
    autor_id = escolher_ou_adicionar(cursor, conexao, "autor", "autor")
    tipo_id = escolher_ou_adicionar(cursor, conexao, "tipo_midia", "tipo de mídia")
    descricao = input("Descrição: ").strip()
    paginas = input("Número de páginas (deixe em branco se não se aplicar): ").strip()
    data_publicacao = input("Data de publicação (YYYY-MM-DD): ").strip()
    
    paginas = int(paginas) if paginas.isdigit() else None

    cursor.execute("""
        INSERT INTO midia (titulo, id_autor, id_tipo, descricao, paginas, data_publicacao)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, autor_id, tipo_id, descricao, paginas, data_publicacao))

    midia_id = cursor.lastrowid

    temas = escolher_temas(cursor, conexao)
    for tema_id in temas:
        cursor.execute("INSERT INTO midia_tema (id_midia, id_tema) VALUES (?, ?)", (midia_id, tema_id))

    conexao.commit()
    conexao.close()
    print("Mídia adicionada com sucesso!")

if __name__ == "__main__":
    adicionar_midia()

