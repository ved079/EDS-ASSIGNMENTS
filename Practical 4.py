import pandas as pd
df = pd.read_csv("imdb data.csv")
print(df)
print(df[['Series_Title','Released_Year']])
print(df.describe())
print(df.mean())
print(df.median())
print(df.loc[df["Meta_score"].max()])
print(df["No_of_Votes"].describe())
print(df.count())
print(df.loc[df['IMDB_Rating']>9])
print(df.loc[ (df['IMDB_Rating']>8) & (df['No_of_Votes'] <689845) ])
print(df.iloc[::-1])
print(df.groupby('Runtime').count())
df.groupby('Certificate').get_group('A')
df.head(20)
df.tail(20)
print(df.groupby('Directo').count())
df['Meta_score'].value_counts()
df['Star2']
df['Star1']
df['Series_Title']
[df['IMDB_Rating'].max()]
