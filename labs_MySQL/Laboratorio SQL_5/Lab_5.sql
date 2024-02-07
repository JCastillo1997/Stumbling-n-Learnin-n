-- Determine the number of copies of the film "Hunchback Impossible" that exist in the inventory system.
select count(title), f.title from film as f
left join inventory as i
on f.film_id = i.film_id
where title  = 'Hunchback Impossible'

-- select count(film_id) from inventory where film_id = (select film_id from film where title= 'Hunchback Impossible')
/*
Me encontraba incapaz de hacer el ejercicio metiendo una subquery, tras obtener el resultado
gracias a chat gpt y ver que es menos claro que usar un join normal adjunto la solución como comentario.
*/

-- List all films whose length is longer than the average length of all the films in the Sakila database.
select title from film where film.length > (select avg(film.length) from film)

-- Use a subquery to display all actors who appear in the film "Alone Trip".

select a.first_name,a.last_name,f.title from actor as a
left join film_actor as fa
on a.actor_id = fa.actor_id
left join film as f
on fa.film_id = f.film_id
where f.title ='Alone Trip'

-- Con subqueries, agradecimientos a Diana.

select first_name, last_name 
from (select * from film  where film.title ='Alone Trip') as pe

left join film_actor as fa
on  pe.film_id = fa.film_id

left join actor as a
on fa.actor_id = a.actor_id

