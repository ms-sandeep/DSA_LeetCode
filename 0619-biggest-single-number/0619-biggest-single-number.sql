# Write your MySQL query statement below
with uniqueNumber as(
    select num 
    from MyNumbers
    group by num
    having count(*)=1
)
select Max(num) as num
from uniqueNumber;