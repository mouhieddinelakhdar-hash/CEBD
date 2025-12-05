DROP TRIGGER IF EXISTS trg_equipe_min_deux;
-- drop trigger first then all whaht we need is to verfier that the number of sportifs after deleteing is always > 2 else we raise
CREATE TRIGGER trg_equipe_min_deux
AFTER DELETE ON Membre_Equipe
FOR EACH ROW
BEGIN
    SELECT
        CASE
            WHEN (SELECT COUNT(*)
                  FROM Membre_Equipe
                  WHERE numEq = OLD.numEq) < 2
            THEN
                RAISE(ABORT, 'Une équipe doit avoir au moins deux membres.')
        END;
END;