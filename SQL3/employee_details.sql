/* List the following details of each employee: employee number, last name, first name, gender, and salary. */

select emp_no, first_name, last_name,  gender, slr.salary
from Employees emp
join Salaries slr on emp.emp_no = slr.emp_no