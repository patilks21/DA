import pandas as pd
import matplotlib.pyplot as pl
df=pd.read_csv("iris.data",names=["sepal_length","sepal_width","petal_length","petal_width","class"])
print(df.describe(include='all'))
print(df.dtypes)
print(df.nunique())
print(df.info())
df.hist(['sepal_length'])
df.hist(['sepal_width'])
df.hist(['petal_length'])
df.hist(['petal_width'])
pl.show()
df.boxplot()
df.plot.scatter(x='sepal_length',y='sepal_width')
df.plot.scatter(x='sepal_length',y='petal_length')
df.plot.scatter(x='sepal_length',y='petal_width')
df.plot.scatter(x='petal_length',y='petal_width')
df.plot.scatter(x='petal_length',y='sepal_width')
df.plot.scatter(x='petal_width',y='sepal_width')
pl.show()

