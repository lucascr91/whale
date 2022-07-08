import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://lucas:1234@db:5432/basedosdados_dev'

db = create_engine(conn_string)
conn = db.connect()

query = '''
SELECT * 
FROM basedosdados_dev.public.iris
LIMIT 10;
'''
df = pd.read_sql_query(query,con=conn)

print(df.to_markdown(index=False))