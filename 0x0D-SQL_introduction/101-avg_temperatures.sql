-- Import dump into hbtn_0c_0 and  displays avg temp by city ordered by temp (desc)
SELECT `city`, AVG(`value`) AS avg_temp FROM `temperatures`
GROUP BY city ORDER BY avg_temp DESC;
