/*Q1*/
select site_id, count(distinct user_id) as number from Q1 
where country_id='BDV'
group by site_id;

/*Q2*/
select user_id, site_id, count(site_id) as visit_num from Q1
where ts>='2019-02-03 00:00:00' and ts<='2019-02-04 23:59:59'
group by user_id, site_id
having visit_num>10;

/*Q3*/
select site_id, count(distinct user_id) as user_num from
(select user_id, site_id from Q1
group by user_id
having max(ts)) as last_visit
group by site_id
order by user_num desc;

/*Q4*/
select count(first.user_id) from
(select user_id, site_id as first_site from Q1 group by user_id having min(ts)) as first
join 
(select user_id, site_id as last_site from Q1 group by user_id having max(ts)) as last
on first.user_id=last.user_id
where first_site=last_site;