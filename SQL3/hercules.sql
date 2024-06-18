/* List all employees whose first name is "Hercules" and last names begin with "B." */

select * 
from Employees
where first_name = 'Hercules' and last_name like 'B.%' 
