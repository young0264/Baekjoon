#입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 
#ID 순으로 조회하는 SQL문을 작성해주세요.
select ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
from ANIMAL_OUTS
left join ANIMAL_INS
on ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_INS.ANIMAL_ID IS NULL
order by ANIMAL_ID