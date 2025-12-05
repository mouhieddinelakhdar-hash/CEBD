import sqlite3, pandas
from sqlite3 import IntegrityError

# Fonction permettant de lire le fichier Excel des JO et d'insérer les données dans la nouvelle base
def read_excel_file_V0(data: sqlite3.Connection, file):
    cursor = data.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # =========================
    # 1) Lecture des sportifs + équipes (onglet LesSportifsEQ)
    # =========================
     # Lecture de l'onglet du fichier excel LesSportifsEQ, en interprétant toutes les colonnes comme des strings
    # pour construire uniformement la requête
    df_sportifs = pandas.read_excel(file, sheet_name='LesSportifsEQ', dtype=str)
    df_sportifs = df_sportifs.where(pandas.notnull(df_sportifs), None)

    for ix, row in df_sportifs.iterrows():
        try:
           
            if row['numSp'] is not None:
                numSp       = int(row['numSp'])
                nomSp       = row['nomSp']
                prenomSp    = row['prenomSp']
                pays        = row['pays']
                spCat       = row['categorieSp']      
                dateNaisSp  = row['dateNaisSp']

                cursor.execute(
                    """
                    INSERT OR IGNORE INTO Sportifs(numSp, nomSp, prenomSp, dateNaisSp, spCat, pays)
                    VALUES (?, ?, ?, ?, ?, ?);
                    """,
                    (numSp, nomSp, prenomSp, dateNaisSp, spCat, pays)
                )

            if row['numEq'] is not None:
                numEq = int(row['numEq'])
                pays  = row['pays']

                cursor.execute(
                    """
                    INSERT OR IGNORE INTO Equipes(numEq, pays)
                    VALUES (?, ?);
                    """,
                    (numEq, pays)
                )
            if (row['numSp'] is not None) and (row['numEq'] is not None):
                numSp = int(row['numSp'])
                numEq = int(row['numEq'])

                cursor.execute(
                    """
                    INSERT OR IGNORE INTO Membre_Equipe(numSp, numEq)
                    VALUES (?, ?);
                    """,
                    (numSp, numEq)
                )

        except IntegrityError as err:
            print(f"Erreur d'intégrité (LesSportifsEQ) : {err} pour la ligne {ix}")
        except Exception as err:
            print(f"Erreur inattendue (LesSportifsEQ) : {err} pour la ligne {ix}")

    
    df_epreuves = pandas.read_excel(file, sheet_name='LesEpreuves', dtype=str)
    df_epreuves = df_epreuves.where(pandas.notnull(df_epreuves), None)

    for ix, row in df_epreuves.iterrows():
        try:
            numEp  = int(row['numEp'])
            nomEp  = row['nomEp']
            nomDi  = row['nomDi']
            formeEp = row['formeEp']        
            categorieEp = row['categorieEp']  
            nbSportifsEp = row['nbSportifsEp']
            dateEp = row['dateEp']


            if nbSportifsEp is not None:
                nbMax = int(nbSportifsEp)
            else:
                nbMax = None

        
            cursor.execute(
                """
                INSERT OR IGNORE INTO Disciplines(nomDi)
                VALUES (?);
                """,
                (nomDi,)
            )

            cursor.execute(
                """
                INSERT OR IGNORE INTO Epreuves(numEp, nomDi, nomEp, sexe, nbMax, catEp, dateEp)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """,
                (numEp, nomDi, nomEp, categorieEp, nbMax, formeEp, dateEp)
            )

        except IntegrityError as err:
            print(f"Erreur d'intégrité (LesEpreuves) : {err} pour la ligne {ix}")
        except Exception as err:
            print(f"Erreur inattendue (LesEpreuves) : {err} pour la ligne {ix}")
   
   
   
   
   
   