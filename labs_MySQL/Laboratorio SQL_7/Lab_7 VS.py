import pandas as pd

pd.set_option('display.max_columns', None)

from sqlalchemy import create_engine


str_conn = 'mysql+pymysql://root:jaime1997@127.0.0.1:3306'

cursor = create_engine(str_conn)

cursor.execute('drop database if exists apps;')

