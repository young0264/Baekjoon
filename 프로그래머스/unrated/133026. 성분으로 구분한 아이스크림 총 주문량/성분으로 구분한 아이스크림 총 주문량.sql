# -- 코드를 입력하세요
# SELECT ICECREAM_INFO.INGREDIENT_TYPE from icecream_info a
# left join first_half b
# where sum (a.ingredient_type)

select b.ingredient_type, sum(total_order) from first_half a
left join icecream_info b
on a.flavor = b.flavor
group by b.ingredient_type
order by a.total_order