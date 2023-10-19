-- Imports temperatures.sql into hbtn_0c_0-- displays top 3 cities temp during Aug and July in desc
SELECT `city`, AVG(`value`) AS avg_temp FROM `temperatures`
WHERE `month`=7 or `month`= 8 
GROUP BY city ORDER BY avg_temp
LIMIT 3;
