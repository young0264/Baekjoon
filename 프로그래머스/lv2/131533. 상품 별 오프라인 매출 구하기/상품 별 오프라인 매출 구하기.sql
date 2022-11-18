-- 코드를 입력하세요 product id
-- 상품 코드별 배출액
SELECT PRODUCT_CODE , sum(price*offline_sale.sales_amount) as SALES from product
left join offline_sale
on product.product_id = offline_sale.product_id
group by product.product_code
order by sales desc, product.product_code