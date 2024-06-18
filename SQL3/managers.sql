/* List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates. */

select dpm.dept_no, dp.dept_name, dmp.emp_no, emp.first_name, emp.last_name, dpm.from_date, dpm.to_date
from Dept_Manager dpm
join Departments dp on dp.dept_no = dpm.dept_no
join Employees emp on emp.emp_no = dpm.emp_no
