(
        SELECT city,
               length(city) l
          FROM station
         ORDER BY l ASC, city
         LIMIT 1
       )
 UNION (
        SELECT city,
               length(city) l
          FROM station
         ORDER BY l DESC, city
         LIMIT 1
       );