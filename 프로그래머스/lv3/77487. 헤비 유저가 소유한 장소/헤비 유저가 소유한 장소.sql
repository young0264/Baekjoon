-- 코드를 입력하세요

# SELECT count(t1.id) as cc, t1.name, (t1.host_id)  #count(t1.host_id )>1
# from places as t1
# group by host_id
# having count(cc)>1

SELECT t1.id, t1.name, (t1.host_id) FROM places as t1
inner join (select count(id) as cc, host_id from places group by (host_id) having (cc)>1 ) as t2
on t1.host_id = t2.host_id
order by t1.id