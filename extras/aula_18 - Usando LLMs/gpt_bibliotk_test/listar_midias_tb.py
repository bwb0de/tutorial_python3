import sqlite3
from tabulate import tabulate

def listar_midias_tabela():
    conexao = sqlite3.connect("midias.db")
    cursor = conexao.cursor()

    consulta = """
    SELECT 
        m.id, m.titulo, a.nome AS autor, t.nome AS tipo, m.data_publicacao
    FROM midia m
    JOIN autor a ON m.id_autor = a.id
    JOIN tipo_midia t ON m.id_tipo = t.id
    ORDER BY m.titulo;
    """

    cursor.execute(consulta)
    midias = cursor.fetchall()

    if not midias:
        print("Nenhuma mídia cadastrada.")
    else:
        tabela = []
        for midia in midias:
            midia_id, titulo, autor, tipo, data_publicacao = midia
            
            # Buscar os temas associados a essa mídia
            cursor.execute("""
                SELECT t.nome 
                FROM tema t
                JOIN midia_tema mt ON t.id = mt.id_tema
                WHERE mt.id_midia = ?
            """, (midia_id,))
            
            temas = [row[0] for row in cursor.fetchall()]
            temas_str = ", ".join(temas) if temas else "Nenhum"

            tabela.append([midia_id, titulo, autor, tipo, data_publicacao if data_publicacao else "Não informada", temas_str])

        print(tabulate(tabela, headers=["ID", "Título", "Autor", "Tipo", "Data de Publicação", "Temas"], tablefmt="grid"))

    conexao.close()

if __name__ == "__main__":
    listar_midias_tabela()

