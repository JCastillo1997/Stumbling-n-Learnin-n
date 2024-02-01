#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[9]:


url='https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv'
datos_tabla= pd.read_csv(url)


# In[11]:


datos_tabla


# In[15]:


# entender la dimensión del archivo(tablas y columnas)
datos_tabla.shape


# In[17]:


datos_tabla.info()
# Analizando las variables consideramos que son apropiadas, las referencias de los clientes,su residencias, su genero y nivel de estudios, ingresos y la prima del seguro junto con el tipo de coche y la claim o parte de cuantía dineraria


# In[45]:


datos_tabla['Customer Lifetime Value'].unique()


# In[40]:


datos_tabla['Customer Lifetime Value'].nunique()


# In[47]:


datos_tabla.nunique()


# In[48]:


datos_tabla.GENDER.unique()
# encontramos que en las columnas con pocas variables unicas hay multiples erratas.


# In[53]:


# extraemos ahora los datos de media, moda y 
print(datos_tabla['Total Claim Amount'].mean())
print(datos_tabla['Total Claim Amount'].mode())
print(datos_tabla['Total Claim Amount'].median())


# In[56]:


datos_tabla.dropna() 
#descubrimos que, aunque perdamos datos relevantes la tabla esta muy incompleta con muchos valores NaN


# In[64]:


datos_tabla.describe()


# In[65]:


# la función describe saca la media, y la moda ademas de los percentiles, utiles para determinar sobre todo como en terminos de salario la media del salario y la moda se de espacian porque hay disparidad.


# In[67]:


# Challenge 2, encontramos 


# In[86]:


datos_tabla=datos_tabla[:1071]
datos_tabla.shape


# In[92]:


datos_tabla.sort_values('ST', ascending=True)
datos_tabla


# In[89]:


datos_tabla.select_dtypes(include='AZ').head()


# In[101]:


datos_tabla['ST'].value_counts()


# In[102]:


# de aqui sacamos que el estado con mas vehiculos vendidos es Oregon, de aqui se ordenan de mas a menos.


# In[103]:


datos_tabla['Policy Type'].value_counts()


# In[100]:


# de aqui sabemos que  el auto personal es el mas registrado


# In[107]:


datos_tabla['GENDER'].value_counts()


# In[108]:


get_ipython().run_line_magic('pinfo', 'types')

    Use loc to create two dataframes: one containing only Personal Auto policies and one containing only Corporate Auto policies.
    Calculate the average income for each policy.
    Print the results.



# In[118]:


data_compa=datos_tabla[['Policy Type','Income']]
data_compa


# In[131]:


Personal=datos_tabla.loc[datos_tabla['Policy Type']== 'Personal Auto']
Personal_2=datos_tabla.loc[datos_tabla['Policy Type']== 'Corporate Auto']
# Aqui separamos por tipo de auto


# In[144]:


Personal['Income'].mean()


# In[146]:


Personal_2['Income'].mean()


# In[147]:


# Eh, aqui las medias, ganan mas los que tienen coche corporativo.


# In[ ]:




