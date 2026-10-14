USE Vrinda

--select , top, order by, show 10 latest sales dilivered  above 1000 rs

SELECT TOP 10 sale_id, order_id,order_date,sales_channel,amount
FROM Vrinda_sales
WHERE order_status='Delivered'
	and amount>1000
ORDER BY order_date DESC , amount DESC;


-- SHOW SALES DETAIL WITH PRODUCT CATEGORY AND SIZE 

SELECT TOP 25 s.sale_id,s.order_id,s.order_date,s.sales_channel, s.amount
FROM Vrinda_sales as s
INNER JOIN Vrinda_product as p
	ON s.sku=p.sku
ORDER BY s.order_date DESC;