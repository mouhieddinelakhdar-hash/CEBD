Dans ce projet, la base SQLite doit être créée à partir du script SQL v0_createDB.sql.
Comme la commande sqlite3 n’est pas disponible dans mon environnement (WSL sans droits sudo), j’ai choisi d’exécuter le script SQL directement via Python, en utilisant un petit programme d’initialisation.

Cette solution fonctionne exactement comme un appel sqlite3 < fichier.sql, mais sans dépendre d’outils externes.

Pour créer la base, il suffit d’exécuter :
 rm data/lesjeux.db
python3 init_db.py


Cela génère automatiquement le fichier :

data/lesjeux.db


et y crée toutes les tables définies dans le script SQL.