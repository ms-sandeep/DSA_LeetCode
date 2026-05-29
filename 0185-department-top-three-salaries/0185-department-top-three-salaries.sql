select d.name as Department, e.name as Employee, e.salary as Salary from
(select*, dense_rank()over(partition by departmentId order by Salary desc) 
as Rank_salary from employee) as e
 join department d on e.departmentId=d.id
where Rank_salary<=3;