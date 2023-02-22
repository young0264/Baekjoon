# select CAR_ID, AVERAGE_DURATION
#     from (select CAR_ID, ROUND(AVG(END_DATE-START_DATE+1),1) AS AVERAGE_DURATION
#             from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#                 group by CAR_ID) T1
#         where AVERAGE_DURATION >= 7
#             order by AVERAGE_DURATION desc, car_id desc
            
            
            
            
select CAR_ID, ROUND(AVG(DATEDIFF(END_DATE,START_DATE)+1),1) AS AVERAGE_DURATION
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        group by CAR_ID            
            having AVERAGE_DURATION > 7
                order by AVERAGE_DURATION desc, car_id desc

# select END_DATE-START_DATE , end_date, start_date
#     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#         group by car_id