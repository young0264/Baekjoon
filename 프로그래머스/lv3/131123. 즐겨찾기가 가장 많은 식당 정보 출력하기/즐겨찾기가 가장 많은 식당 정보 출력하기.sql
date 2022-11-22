-- 코드를 입력하세요
# SELECT food_type, rest_id, rest_name, max(favorites) as favorites from rest_info
# group by food_type 
# order by food_type desc


SELECT rest_info.food_type, rest_info.rest_id, rest_info.rest_name, rest_info.favorites
from rest_info
join (select food_type, max(favorites) as ff
      from rest_info 
      group by food_type) as new_rest_info
on rest_info.food_type = new_rest_info.food_type and rest_info.favorites = new_rest_info.ff
order by food_type desc