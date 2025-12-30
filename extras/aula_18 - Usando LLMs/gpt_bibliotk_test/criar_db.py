import sqlite3

def criar_banco():
    conexao = sqlite3.connect("midias.db")
    cursor = conexao.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS tipo_midia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS autor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS midia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        id_autor INTEGER NOT NULL,
        id_tipo INTEGER NOT NULL,
        descricao TEXT,
        paginas INTEGER,
        data_publicacao DATE,
        FOREIGN KEY (id_autor) REFERENCES autor(id),
        FOREIGN KEY (id_tipo) REFERENCES tipo_midia(id)
    );

    CREATE TABLE IF NOT EXISTS tema (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS midia_tema (
        id_midia INTEGER NOT NULL,
        id_tema INTEGER NOT NULL,
        PRIMARY KEY (id_midia, id_tema),
        FOREIGN KEY (id_midia) REFERENCES midia(id) ON DELETE CASCADE,
        FOREIGN KEY (id_tema) REFERENCES tema(id) ON DELETE CASCADE
    );
    """)

    conexao.commit()
    conexao.close()
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    criar_banco()

