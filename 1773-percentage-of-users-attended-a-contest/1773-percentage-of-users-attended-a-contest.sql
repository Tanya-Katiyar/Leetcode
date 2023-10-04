# Write your MySQL query statement below
# SELECT contest_id
#     , ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage
# FROM Register 
# GROUP BY contest_id
#     ORDER BY percentage DESC, contest_id







select contest_id, round( count(user_id)*100/ (select count(user_id) from users)  ,2)
as percentage from Register group by contest_id order by percentage desc, contest_id;







