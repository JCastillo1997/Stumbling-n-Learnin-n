-- List the number of films per category.
select COUNT(film_id) as 'Numero de films', max(category_id) as 'categorias'
from film_category
group by category_id;