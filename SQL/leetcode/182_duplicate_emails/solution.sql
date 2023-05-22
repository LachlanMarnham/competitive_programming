SELECT email "Email"
  FROM person
 GROUP BY email
HAVING count(email) > 1;