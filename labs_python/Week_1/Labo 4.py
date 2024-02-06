#!/usr/bin/env python
# coding: utf-8

# In[170]:


products=('lista','tetera','botella','ventilador','poligrafo')


# In[201]:


def customer_orders():
    try:
        n_pedidos = int(input('introduce el numero de pedidos'))
        if n_pedidos>0:
            ordenes_1=set(input('introduce qque pedidos') for _ in range(n_pedidos))
            return ordenes_1
        else:
            print('no es valido')
    except ValueError:
            print('feeffeeffe')


# In[210]:


def productos_inventario(products):
    inventario= {}
    for product in products:
        try:
            value=int(input(f'cuanto vale{product}'))
            
            if value<=0:
                
                print('como lo quieres gratis no lo añado')
                product.remove(value)
        except ValueError:
            print('eso no es ni un numero')
        else:
            inventario[product]=value
        finally:
             _
    return inventario
         


# In[218]:


def price_diff(order_client):
    lst=[]
    
    try:
        
        while len(lst)!=(customer_order):
            orden= int(input(f'introduce el precio del producto'))
            if order>0:
                lst.append(order)
            else:
                print('ole')
    except ValueError:
        print('Noup')
    return sum(lst)
                    
                            


# In[ ]:




