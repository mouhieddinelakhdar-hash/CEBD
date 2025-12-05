import sqlite3

DB_NAME = "data/lesjeux.db"

def run_sql_script(path):
    # Lire le fichier SQL
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()

    # Se connecter à la base (ou la créer si elle n'existe pas)
    conn = sqlite3.connect(DB_NAME)

    try:
        conn.executescript(sql)
        conn.commit()
        print("Base créée et script exécuté avec succès !")
    except Exception as e:
        print("Erreur lors de l'exécution du script :", e)
    finally:
        conn.close()

if __name__ == "__main__":
    run_sql_script("data/v0_createDB.sql")
