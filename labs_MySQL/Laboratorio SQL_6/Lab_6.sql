/*
Step 1: Create a View
First, create a view that summarizes rental information for each customer.
The view should include the customer's ID, name, email address, and total number of rentals (rental_count).
*/
create view exercise_1 as
select customer_id,concat(first_name," ",last_name) as nombre,
email, count(rental_id) as times_rented
from customer 
join rental using (customer_id)
group by customer_id
order by times_rented

/*
Step 2: Create a Temporary Table
Next, create a Temporary Table that calculates the total amount paid by each customer (total_paid). 
The Temporary Table should use the rental summary view created in Step 1 to join with the payment table
 and calculate the total amount paid by each customer.
 */
create temporary table gastos_1
select customer_id,nombre,sum(amount) as total_spent from exercise_1
join payment using (customer_id)
group by customer_id
order by total_spent

/*
Step 3: Create a CTE and the Customer Summary Report
Create a CTE that joins the rental summary View with the customer payment summary Temporary Table created in Step 2.
The CTE should include the customer's name, email address, rental count, and total amount paid.
*/
with CTE_table as
(select e.customer_id,e.nombre,email,`times rented`,total_spent from exercise_1 as e
join gastos_1 as g
on e.customer_id =g.customer_id )
select * from CTE_table

/*
Next, using the CTE, create the query to generate the final customer summary report,
which should include: customer name, email, rental_count, total_paid and average_payment_per_rental,
this last column is a derived column from total_paid and rental_count.
*/
with CTE_table as
(select e.customer_id,e.nombre,email,round(total_spent/`times rented`,2) as beneficios_tiempo from exercise_1 as e
join gastos_1 as g
on e.customer_id =g.customer_id )
select * from CTE_table