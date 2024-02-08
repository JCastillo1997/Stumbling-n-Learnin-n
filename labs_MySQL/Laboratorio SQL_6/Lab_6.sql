/*
Step 1: Create a View
First, create a view that summarizes rental information for each customer.
The view should include the customer's ID, name, email address, and total number of rentals (rental_count).
*/
select customer_id,concat(first_name," ",last_name) as nombre,email, count(rental_id) as "times rented"
from customer 
join rental using (customer_id)
group by customer_id
order by "times rented"

