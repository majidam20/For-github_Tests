
## Instructions to develop the solutions

This directory contains some files that can be used to develop your solution
for the case study.

There's a directory where you can drop your solution files and a command that
you can use to check their results against the expected output, giving you
feedback about them.

This is how it works:

  * Launch the Docker packaged PostgreSQL database server with:
    ```
    docker-compose up
    ```

  * Put your solution files in `src/solution` (Eg. `src/solution/task1.sql`).

  * For each solution file run `docker-compose exec case-study check <task-name>` (Eg. `check task1`).

There are other directories inside `src/` that can be interesting to you:

* `init-fixtures`: contains the scripts that are necessary to initialize the
  database. Every time you check a solution script, the whole database gets
  dropped and regenerated using these fixtures.

* `solution`: contains your solution files.

* `output-obtained`: contains the latest execution results of your solutions in
  CSV format.

* `output-expected`: contains the expected results from each query in CSV
  format.

**Note:** To know the exact name you have to use for your solutions, you can
check the filenames in the `output-expected` folder. The files there should
match the files in the `solution` folder.

## Instructions to submit the solution

Please submit a modified compressed file including an SQL file for each of the 
tasks in `src/solution/`