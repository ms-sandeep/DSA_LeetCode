SELECT customer_number 
FROM Orders
group by customer_number
order by Count(*) desc
limit 1;
 