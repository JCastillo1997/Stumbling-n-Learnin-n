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
select round(avg(film.length))from film
-- Esta te saca la media de longitud en minutos.
SELECT DATEDIFF(max(rental_date),min(rental_date))
as Diferencia
from rental
-- Esta te saca la diferencia entre el max y el min
date_format(convert(rental_date,DATE), '%M') as 'Month',
date_format(convert(rental_date,DATE), '%a') as 'Weekday'
-- Esto te lo convierte
select distinct count(title) from film
-- Esto te da la cuenta
select distinct count(title)
from film
where rating = 'r'
-- Esta formula es solo cambiar el string de 'r' por los otros valores de rating tal que asi
select distinct count(title)
from film
where rating = 'PG'
select distinct count(title)
from film
where rating = 'G'
select distinct count(title)
from film
where rating = 'NC-17'
---
select distinct count(title), rating as 'Rating'
from film
Group by rating
order by count(title) desc
-- Esto te da la lista ordenada.
select avg(length), rating
from film
Group by rating
order by avg(length) desc
-- Esto te da la lista ordenada por rating y la duracion media de la peli por rating.
select avg(length), rating
from film
GROUP BY rating
HAVING avg(length) > 120
order by avg(length) desc
-- Esto ultimo te da las que tienen longitud media mas larga que 120 mins, preguntar a Yona porque no iba con el Where 
-- y he tenido que poner un HAVING