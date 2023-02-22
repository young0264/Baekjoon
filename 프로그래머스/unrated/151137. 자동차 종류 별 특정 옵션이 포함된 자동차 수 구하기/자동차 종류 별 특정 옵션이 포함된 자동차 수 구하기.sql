-- 코드를 입력하세요
select car_type,count(car_type) from(
SELECT car_id, car_type
    from CAR_RENTAL_COMPANY_CAR 
        where( options like '%통풍시트%' 
        or options like '%선시트%'        
        or options like '%가죽시트%')
)
    group by car_type
    order by car_type asc