-- 코드를 입력하세요
SELECT t3.apnt_no, t1.pt_name, t3.pt_no, t3.MCDP_CD, t2.dr_name ,t3.apnt_ymd 
from appointment as t3
join (select * from patient) as t1 
on t1.pt_no = t3.pt_no

join (select * from doctor) as t2
on t2.dr_id = t3.mddr_id

where  
    DATE_FORMAT(t3.apnt_ymd, '%Y-%m-%d') = '2022-04-13'
    and t3.APNT_CNCL_YN = 'N'
    and t3.mcdp_cd = 'CS'
    
order by t3.apnt_ymd

# and APNT_YMD like '2022-04-13%'