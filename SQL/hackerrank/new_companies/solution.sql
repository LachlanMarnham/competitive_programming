SELECT company.company_code,
       company.founder,
       count(DISTINCT lead_manager.lead_manager_code),
       count(DISTINCT senior_manager.senior_manager_code),
       count(DISTINCT manager.manager_code),
       count(DISTINCT employee.employee_code)
  FROM company
 INNER JOIN lead_manager
    ON company.company_code = lead_manager.company_code
 INNER JOIN senior_manager
    ON company.company_code = senior_manager.company_code
 INNER JOIN manager
    ON company.company_code = manager.company_code
 INNER JOIN employee
    ON company.company_code = employee.company_code
 GROUP BY company.company_code,
          company.founder
 ORDER BY company.company_code ASC;