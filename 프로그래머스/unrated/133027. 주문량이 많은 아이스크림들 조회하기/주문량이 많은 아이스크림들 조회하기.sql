-- 코드를 입력하세요
SELECT t1.flavor from first_half as t1
join (select july.total_order, july.flavor from july) as t2
on t1.flavor = t2.flavor
group by flavor
order by sum(t1.total_order) + sum(t2.total_order) desc
limit 3