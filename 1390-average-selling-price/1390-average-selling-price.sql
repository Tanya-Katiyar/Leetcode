# Write your MySQL query statement below
SELECT a.product_id, ifnull(ROUND(SUM(b.units*a.price)/SUM(b.units),2),0) as average_price
FROM Prices as a
LEFT JOIN UnitsSold as b
ON a.product_id=b.product_id AND (b.purchase_date BETWEEN a.start_date AND a.end_date)
GROUP BY product_id;




# select p.product_id, round( sum(p.price*u.units)/ sum(u.units) ,2)
# as average_price from Prices p join UnitsSold u on p.product_id=u.product_id and (u.purchase_date between p.start_date and p.end_date)
# group by product_id;









