-- Ignore duplicate rows
select count(*) --from df_2022_09_16 d 
from(
select distinct *
from df_2022_09_16 d16
)
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get sum Likes in each "Page Name" groups
select "Page Name", sum("Likes") sum_likes
from df_2022_09_16 d16
group by "Page Name"
order by sum_likes desc
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get sum Angries in each "Page Name" groups 
select "Page Name", sum("Angry") sum_angry
from df_2022_09_16 d16
group by "Page Name"
order by sum_angry desc
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get sum Angries in each "Page Name", "Page Category" groups
select "Page Name", "Page Category",  sum("Angry") sum_angry
from df_2022_09_16 d16
group by "Page Name", "Page Category"
order by sum_angry desc
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get count Page Admin Top Country in each "Page Name" , "Page Admin Top Country" groups
select "Page Name" , "Page Admin Top Country" PATC, count("Page Admin Top Country") count_PATC 
from df_2022_09_16 d16
group by "Page Name", PATC
order by  count_PATC
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get count Page Category  in each "Page Admin Top Country" PATC, "Page Category" groups
select "Page Admin Top Country" PATC, "Page Category" , count("Page Category") count_PageCategory
from df_2022_09_16 d16
group by  PATC, "Page Category"
order by  count_PageCategory desc 
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get count Facebook Id in each "Page Name" PN, "Facebook Id" groups
select "Page Name" PN, "Facebook Id" FBId, count("Facebook Id") count_FBId  
from df_2022_09_16
group by PN, FBId 
order by count_FBId desc 
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get sum Likes in each "Page Category" groups
select "Page Category", sum("Likes") sum_Likes
from df_2022_09_16 d16
group by  "Page Category"
order by  sum_Likes desc 
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get sum Angries in each "Page Category" groups
select "Page Category", sum("Angry") sum_Angry
from df_2022_09_16 d16
group by  "Page Category"
order by  sum_Angry desc 
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get sum Shares for each "Facebook Id" groups
select "Facebook Id", sum("Shares") sum_Shares
from df_2022_09_16 d16
group by  "Facebook Id"
order by  sum_Shares desc 
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get sum Shares for each "Page Category" groups and insert in the new table
create table if not exists "PageCategory_sum_Shares" as
select "Page Category", sum("Shares") sum_Shares
from df_2022_09_16 d16
group by  "Page Category"
order by  sum_Shares desc 
++++++++++++++++++++++++++++++++++++++++++++++++
-- Get groups by "Page Category" and "Post Created Date" then insert in the new table
create table if not exists "PCDate" as
select "Page Category", CAST("Post Created Date" as date) PCDate
from df_2022_09_16 d16
group by  "Page Category", PCDate
order by  "Page Category" 
