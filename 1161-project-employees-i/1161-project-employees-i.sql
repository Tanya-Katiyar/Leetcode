# Write your MySQL query statement below
select project_id, round(avg(experience_years),2) as average_years from Project p inner join Employee e on e.employee_id=p.employee_id group by project_id;









# select p.project_id, round( sum(e.experience_years)/count(e.employee_id) ,2)
# as average_years from Project p inner join Employee e on e.employee_id=p.employee_id group by project_id;









