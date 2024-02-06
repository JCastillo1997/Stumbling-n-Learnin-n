select * from actor
-- Esto escupe todo los datos de la tabla actor
select * from film
-- Esto escupe todos los datos de la tabla filme
select * from customer
-- Esto escupe todos los datos de la tabla customer
select title from film
-- Esto te entrega todos los titulos dentro de film en la columna title
select name from language
-- Esto te vomita todos los lenguajes existentes en la tabla.
select first_name from staff
-- Esto te da la increible plantilla de Mike y Jon, trabajan como siete cada uno.
select distinct release_year from film;
-- Esto te suelta el unico valor de 2006, año de Lady in The Water
select distinct store_id from store;
-- Los valores de id de la tienda, dando por hecho que son únicos.
select distinct last_name  from staff
-- Los unicos apedillos dandonos el valor total
SELECT COUNT(last_name)  FROM staff;
-- y esto da el numero de empleados al darnos el numero de apellidos
select count(rental_id) from rental
-- esto da el numero de films
select distinct(length) from film
order by length desc
-- Esto te da los distincts de la longitud en order descendente que son los valores mas altos
select first_name,last_name from actor
where first_name = 'Scarlett'
-- Esto te devuelve los apellidados Scarlett, ninguno Johannson.
