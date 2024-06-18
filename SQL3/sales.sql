/* List all employees in the Sales department, including their employee number, last name, first name, and department name. */


select emp.emp_no, emp.lst_name, emp.first_name, dp.dept_name
from Employees emp
join Dept_Manager dpm on dpm.emp_no = emp.emp_no
join Departments dp on dp.dept_no = dpm.dept_no
where dp.dept_name = 'Sales'
