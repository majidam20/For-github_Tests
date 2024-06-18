select   strftime('%W', check_out_date) as week, count(strftime('%W',check_out_date)) / 2 as number_of_rooms
from reservations 
group by strftime('%W', check_out_date)