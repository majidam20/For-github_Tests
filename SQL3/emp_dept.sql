/* List the department of each employee with the following information: employee number, last name, first name, and department name. */


select emp.first_name, emp.last_name, dp.dept_name
from Dept_Emp
join Departments dp on dp.dept_no = Dept_Emp.dep_no
join Employees emp on emp.emp_no = Dept_Emp.emp_no
