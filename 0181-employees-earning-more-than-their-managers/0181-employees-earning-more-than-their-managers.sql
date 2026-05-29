select e.name as Employee from employee as e
join employee as el on e.managerId=el.id where e.salary>el.salary; 