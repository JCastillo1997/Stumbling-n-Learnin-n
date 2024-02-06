select title,film.length as "Longest movies"
from film 
order by film.length desc
limit 1
-- Esta función crea las mas films mas largas y las mete a nombre de longest movies
select title,film.length as "Shortest movies"
from film 
order by film.length asc
limit 1
-- Esta función hace lo mismo pero escupe las mas cortas
