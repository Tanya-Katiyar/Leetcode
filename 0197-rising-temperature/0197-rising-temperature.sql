# Write your MySQL query statement below
# select x.id from Weather x, Weather y where x.temperature>y.temperature and DATEDIFF(x.recordDate,y.recordDate)=1; 









select x.id from Weather x, Weather y where x.temperature>y.temperature and DATEDIFF(x.recordDate, y.recordDate)=1;






