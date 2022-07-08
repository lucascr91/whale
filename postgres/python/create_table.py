import pandas as pd
from sqlalchemy import create_engine
from sklearn import datasets

iris = datasets.load_iris()
df=pd.DataFrame(iris.data)

conn_string = 'postgresql://lucas:1234@db:5432/basedosdados_dev'

db = create_engine(conn_string)
conn = db.connect()

df.to_sql('iris', conn, if_exists='replace', index=False)