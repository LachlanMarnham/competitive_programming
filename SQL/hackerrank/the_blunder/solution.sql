SELECT ceil(avg(employees.salary) - avg(miscalculated.wrong_salary))
  FROM employees
 INNER JOIN (
        SELECT id,
               cast(replace(cast(salary AS char(25)), '0', '') AS UNSIGNED) AS wrong_salary
          FROM employees
       ) AS miscalculated
    ON employees.id = miscalculated.id;