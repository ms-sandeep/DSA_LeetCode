select d.name as Department, e.name as Employee, e.salary as Salary from
(select name, departmentId, salary, 
dense_rank() 
over(partition by departmentId order by salary desc) as rnk from employee ) e
inner join department d on e.departmentId=d.id where e.rnk=1;