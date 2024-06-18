### Objective

Data analysis Write SQL queries on employees of the corporation from the 1980s and 1990s.

### Brief

It is a beautiful spring day on Mars, and it is two weeks since you have been hired as a new data engineer. Your first major task is a research project on employees of the corporation from the 1980s and 1990s. You may connect to the database with the following credentials:

| Host        | wookie-db.codesubmit.io |
| ----------- | ----------------------- |
| Database    | hr                      |
| Username    | reader                  |
| Password    | reader                  |

Example using psql: `PGPASSWORD=reader psql -h wookie-db.codesubmit.io -U reader hr`

Once you have a connected to the database, write the following queries, each in its respective file.

### Tasks

-   List the following details of each employee: employee number, last name, first name, gender, and salary.
    Write your query into `employee_details.sql`.

-   List employees who were hired in 1986.
    Write your query into `doh1986.sql`.

-   List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
    Write your query into `managers.sql`.

-   List the department of each employee with the following information: employee number, last name, first name, and department name.
    Write your query into `emp_dept.sql`.

-   List all employees whose first name is "Hercules" and last names begin with "B."
    Write your query into `hercules.sql`.

-   List all employees in the Sales department, including their employee number, last name, first name, and department name.
    Write your query into `sales.sql`.

### Evaluation Criteria

-   SQL best practices
-   Show us your work through your commit history
-   Completeness: did you complete the features?
-   Correctness: does the functionality act in sensible, thought-out ways?



