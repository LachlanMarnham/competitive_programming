SELECT DISTINCT city
  FROM station
 WHERE city like '%a'
    OR city like '%e'
    OR city like '%i'
    OR city like '%o'
    OR city like '%u';