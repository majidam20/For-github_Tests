select h.country , cast (sum (b.number_bookings) as float (4,2)) / SUM  (c.number_clicks) as booking_conversion
from hotels h 
join clicks c on h.hotel_id = c.hotel_id 
join bookings b on b.hotel_id = c.hotel_id 
GROUP by h.country
ORDER by h.country 