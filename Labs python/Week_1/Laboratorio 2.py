#!/usr/bin/env python
# coding: utf-8

# In[ ]:


In the last lab, you were starting an online store that sells various products. To ensure smooth operations, you developed a program that manages customer orders and inventory.

You did so without using flow control. Let's go a step further and improve this code.

Follow the steps below to complete the exercise:

    Look at your code from the lab data structures, and improve repeated code with loops.

    Instead of asking the user to input the name of three products that a customer wants to order, do the following:

    a. Prompt the user to enter the name of a product that a customer wants to order.

    b. Add the product name to the "customer_orders" set.

    c. Ask the user if they want to add another product (yes/no).

    d. Continue the loop until the user does not want to add another product.

    Instead of updating the inventory by subtracting 1 from the quantity of each product, only do it for the products that were ordered (those in "customer_orders").


# In[30]:


products=["t-shirt","mug","hat","book","keychain"]


# In[47]:


x=str(input('de qué '))
if x in products:
    y=int(input('cuantos '))
    inventory[x]=y
else:
    print('aqui no hay')
    
    


# In[3]:


customer_orders=set()


# In[18]:


n=input('quieres algo de la lista ')

while n=='yes':
    m=input('introduce que quieres de la lista ')
    if m in products:
        customer_orders.add(m)
        r=input('algo mas? ')
        if r=='no':
            break
    if m not in products:
        print('sin existencias ')
        break
if n=='no':
    print('understandable, tenga una buena mañana')
    
    
  
    


# In[78]:


for k,v in inventory.items():
    
    inventory[k] = v-1
    


# In[79]:


inventory

