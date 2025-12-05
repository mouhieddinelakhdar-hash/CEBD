DROP TABLE IF EXISTS Participations;
DROP TABLE IF EXISTS Membre_Equipe;
DROP TABLE IF EXISTS Epreuves;
DROP TABLE IF EXISTS Disciplines;
DROP TABLE IF EXISTS Equipes;
DROP TABLE IF EXISTS Sportifs;
-- on doit dabord Drop tous les tables sils exsite deja 

CREATE TABLE Sportifs (
    numSp      INTEGER PRIMARY KEY CHECK (numSp BETWEEN 1000 AND 1500),
    nomSp      TEXT    NOT NULL,
    prenomSp   TEXT    NOT NULL,
    dateNaisSp DATE    NOT NULL,
    spCat      TEXT    NOT NULL CHECK (spCat IN ('masculin', 'feminin')),
    pays       TEXT    NOT NULL,
    UNIQUE (nomSp, prenomSp)
);

CREATE TABLE Equipes (
    numEq INTEGER PRIMARY KEY CHECK (numEq BETWEEN 1 AND 100),
    pays  TEXT    NOT NULL
);

CREATE TABLE Membre_Equipe (
    numSp INTEGER,
    numEq INTEGER,
    PRIMARY KEY (numSp, numEq),
    FOREIGN KEY (numSp) REFERENCES Sportifs (numSp),
    FOREIGN KEY (numEq) REFERENCES Equipes (numEq)
);

CREATE TABLE Disciplines (
    nomDi TEXT PRIMARY KEY
);

CREATE TABLE Epreuves (
    numEp  INTEGER PRIMARY KEY,
    nomDi  TEXT NOT NULL,
    nomEp  TEXT NOT NULL,
    sexe   TEXT NOT NULL CHECK (sexe IN ('masculin', 'feminin', 'mixte')),
    nbMax  INTEGER CHECK (nbMax > 0),
    catEp  TEXT NOT NULL CHECK (catEp IN ('individuelle', 'equipe', 'couple')),
    dateEp DATE NOT NULL,
    FOREIGN KEY (nomDi) REFERENCES Disciplines (nomDi)
);

CREATE TABLE Participations (
    P_ID   INTEGER NOT NULL,
    numEp  INTEGER NOT NULL,
    result TEXT CHECK (result IN ('Or', 'Argent', 'Bronze')),
    PRIMARY KEY (P_ID, numEp),
    FOREIGN KEY (numEp) REFERENCES Epreuves (numEp)
);
DROP VIEW IF EXISTS LesAgesSportifs;

CREATE VIEW LesAgesSportifs AS
SELECT
    numSp,
    nomSp,
    prenomSp,
    pays,
    spCat,
    dateNaisSp,
    CAST((julianday('now') - julianday(dateNaisSp)) / 365.25 AS INTEGER) AS ageSp
FROM Sportifs;

DROP VIEW IF EXISTS LesNbsEquipiers;

CREATE VIEW LesNbsEquipiers AS
SELECT
    numEq,
    COUNT(*) AS nbEquipiersEq
FROM Membre_Equipe
GROUP BY numEq;



