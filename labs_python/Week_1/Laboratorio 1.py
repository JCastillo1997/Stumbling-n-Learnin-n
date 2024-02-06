#!/usr/bin/env python
# coding: utf-8

# In[ ]:


As part of a business venture, you are starting an online store that sells various products. To ensure smooth operations, you need to develop a program that manages customer orders and inventory.

Follow the steps below to complete the exercise:


# In[1]:


# Define a list called `products` that contains the following items: "t-shirt", "mug", "hat", "book", "keychain".

products=["t-shirt","mug","hat","book","keychain"]
products


# In[2]:


# 2. Create an empty dictionary called `inventory`.
inventory={}


# In[48]:


#3. Ask the user to input the quantity of each product available in the inventory. Use the product names from the `products` list as keys in the `inventory` dictionary and assign the respective quantities as values.
x=input('de qué ')
y=input('cuantos ')
if x in products:
    inventory[x]=y
else:
    print('no tenemos')
    


# In[4]:


# 4. Create an empty set called `customer_orders`.
customer_orders=set()


# In[21]:


# 5. Ask the user to input the name of three products that a customer wants to order (from those in the products list, meaning three products out of "t-shirt", "mug", "hat", "book" or "keychain". Add each product name to the `customer_orders` set.

l=input('introduce un elemento de la lista ')
m=input('introduce otro elemento de la lista ')
k=input('el último lo prometo ')
if l and m and k in products:
    customer_orders.add(l)
    customer_orders.add(m)
    customer_orders.add(k)
else:
    print('no')
# 6. Print the products in the `customer_orders` set.
print(customer_orders)
    


# In[28]:


# 7. Calculate the following order statistics:
    #Total Products Ordered: The total number of products in the `customer_orders` set.
    #Percentage of Products Ordered: The percentage of products ordered compared to the total available products.
len(customer_orders)


# In[43]:


# #Percentage of Products Ordered: The percentage of products ordered compared to the total available products.
porcentaje= (len(customer_orders)*100)/len(products)
print('el porcenaje de los elementos solicitados respecto a los totales ofrecidos es',porcentaje, '%')


# In[61]:


# Update the inventory by subtracting 1 from the quantity of each product. Modify the inventory dictionary accordingly.
inventory['t-shirt']-=1
inventory['book']-=1
inventory['hat']-=1
inventory['keychain']-=1
inventory['mug']-=1

    

