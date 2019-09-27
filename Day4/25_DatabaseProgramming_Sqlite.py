from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///RetailInventory.sqlite')

# conn = engine.connect()
# conn.execute('create table products (product_name char(25), price number(5,2))')
# conn.execute('insert into products values ("Sony Bravia 52", 78234.00)')
# conn.execute('insert into products values ("Samsung Galaxy JMax", 19385.00)')
# conn.close()

with engine.connect() as conn1:
    rs = conn1.execute('select product_name, price from products')
    df = pd.DataFrame(rs.fetchall())
    #df = pd.DataFrame(rs.fetchmany(3))

print(df)

tablenames = engine.table_names()
print('\nExisting tables: ', tablenames)

