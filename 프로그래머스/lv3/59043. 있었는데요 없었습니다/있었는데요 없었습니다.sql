-- 코드를 입력하세요
SELECT ANIMAL_INS.ANIMAL_ID,ANIMAL_INS.NAME
FROM ANIMAL_INS
INNER JOIN ANIMAL_OUTS
ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE TIMESTAMPDIFF(SECOND,ANIMAL_INS.DATETIME,ANIMAL_OUTS.DATETIME)<0
ORDER BY ANIMAL_INS.DATETIME