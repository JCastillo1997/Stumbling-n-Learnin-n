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
