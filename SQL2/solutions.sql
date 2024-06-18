## Task 1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


with session as 
(select sum(cpc) as sumss, * from session_sources ss 
group by campaign_id)
,
api as(
select sum (cost) as sumaac, * from api_adwords_costs aac
group by campaign_id)
select CAST(session.sumss as int) as sessionCast, cast(api.sumaac as int) as apiCast, 
session.campaign_id , api.campaign_id
from session
join api on session.campaign_id = api.campaign_id
where sessionCast = apiCast --Comment this line If you want to see all calculated costs
order by session.campaign_id


# Present no inconsistency row with no duplication in key values

select sum(cpc) as sumss, * from session_sources ss 
group by session_id , user_id, event_date
having count (*) > 1
order by session_id


## Task 2 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

select sum(revenue), * from conversions 
group by conv_id, user_id  , conv_date


# Pattern that was detected

select sum(revenue), count(market), * from conversions 
group by conv_id, user_id, conv_date, market
having count(market) > 1


# Present no inconsistency row with no duplication in key values

select count(*), *  from conversions  
group by conv_id, user_id  , conv_date 
having count (*) > 1
order by conv_date 



## Task 3 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


select sum(conv.revenue) as sumConv,sum(cb.revenue) as sumCb, count (conv.market), count (cb.market),
* from conversions conv
join conversions_backend cb 
on conv.conv_id = cb.conv_id 
where conv.revenue = cb.revenue --Comment this line If you want to see all calculated costs
GROUP by conv.market  --c.conv_id , c.user_id, c.conv_date 
--having count (*) > 1
ORDER by count (conv.market) DESC  



## Task 4 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

select count (*) as c1 from attribution_customer_journey attr
group by conv_id, session_id
having count (*) > 1



# Calculate how many of ihc are less than 1 and equal 1 

with AttrLess1 as (
select count (*) as countAttrLess1 from (
select sum (ihc) as sumAttrLess1 from attribution_customer_journey attr
group by conv_id, session_id
having sum (ihc) < 1
) as aac) 
,
AttrEqual1 as (
select count (*) as countAttrEqual1 from (
select sum (ihc) as sumAttrEqual1 from attribution_customer_journey attr
group by conv_id, session_id
having sum (ihc) = 1
) as bbc) 
select * from AttrLess1, AttrEqual1



## Task 5 (Bonus)+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

select * from session_sources ss  
where channel_name like '%[^a-Z0-9]%' or channel_name = NULL


select count(session_id),* from session_sources ss
group by channel_name 
order by session_id 



## Task 6 (Bonus)+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
select count(*), * from session_sources ss
group by campaign_id, user_id, event_date
having count (*) > 1
order by session_id


select sum(cpc),* from session_sources ss
group by market  
order by sum(cpc) DESC 


select sum(cpc),* from session_sources ss
group by channel_name 
order by session_id, user_id, event_date