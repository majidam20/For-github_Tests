select gl.traveler as traveler_name
from guest_list gl 
join travelers t on t.name = gl.traveler 
where t.age  <= 16
group by gl.traveler