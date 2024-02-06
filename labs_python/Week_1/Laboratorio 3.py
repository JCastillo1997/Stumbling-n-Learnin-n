#!/usr/bin/env python
# coding: utf-8

# In[1]:


products=["t-shirt","mug","hat","book","keychain"]
inventory = {}
def initialize_inventory(products):
    for product in products:
        cantidad = int(input(f"introduce numero del {product}: "))
        inventory[product] = cantidad
    return inventory


# In[2]:


customer_orders=set()
def get_customer_orders():
    r=str(input('que quieres pedir de customer_orders '))
    if r in products:
        customer_orders.add(r)
        
    else:
        print('no lo tenemos')
        
    return customer_orders
    
    
        


# In[3]:


def update_inventory(customer_orders, inventory):
    for e in customer_orders:
        if e in inventory.keys():
            inventory[e]-= 1
    return inventory
    
        


# In[4]:


def calculate_order_statistics(customer_orders,products):
    y= (len(customer_orders)*100)/len(products)
    o= len(customer_orders)
    print('el porcentaje de todos los objetos pedidos es',y,'%')
    return y,o
    


# In[5]:


order_statistics=''
def print_order_statistics(order_statistics):
    r=print((len(customer_orders)*100)/len(products))
    y=print(len(customer_orders))
    
    return r,y


# In[6]:


def print_updated_inventory(inventory):
    e=print(inventory)
    return e


# In[7]:


initialize_inventory(products)
get_customer_orders()
update_inventory(customer_orders,inventory)
calculate_order_statistics(customer_orders,products)
print_order_statistics(order_statistics)
print_updated_inventory(inventory)

