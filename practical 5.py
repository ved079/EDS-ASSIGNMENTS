import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('imdb data.csv')
plt.bar(df['Released_Year'],df['IMDB_Rating'])
plt.title('Released_Year vs IMDB_Rating')
plt.xlabel('Released_Year')
plt.ylabel('IMDB_Rating')
plt.show()
d=df['IMDB_Rating']
plt.hist(d,bins=7,edgecolor='black')
plt.xlabel('IMDB_Rating')
plt.ylabel('Gross')
plt.show()
d=df['IMDB_Rating']
plt.hist(d,bins=40,edgecolor='black')
plt.xlabel('IMDB_Rating')
plt.ylabel('No_of_Votes')
plt.show()
d=df['Meta_score']
plt.hist(d)
plt.xlabel('Meta_score')
plt.ylabel('Runtime')
plt.show()
b=df['Meta_score']
plt.hist(b,bins=12,edgecolor='black')
plt.xlabel('Meta_score')
plt.ylabel('IMDB_Rating')
plt.show()
year=df['Released_Year'].tolist()
year=set(year)
year=list(year)
noofmodels=[]
for i in range(len(year)):
 a=df.groupby('Released_Year').get_group(year[i])
 b=len(a)
 noofmodels.append(b)
plt.pie(noofmodels,labels=year)
plt.title('Chart of cars launched per year')
plt.show()

mpg=df['Genre'].tolist()
mpg=set(mpg)
mpg=list(mpg)
noofcars=[]
for i in range(len(year)):
 a=df.groupby('Genre').get_group(mpg[i])
 b=len(a)
 noofcars.append(b)
plt.pie(noofcars)
plt.title('Genre')
plt.show()
d=df['Meta_score']
e=df['IMDB_Rating']
plt.scatter(e,d)
plt.ylabel('Meta_score')
plt.xlabel('IMDB_Rating')
plt.show()
d=df['IMDB_Rating'].tolist()
d=set(d)
d=list(d)
d.sort()
accelerate=[]
for i in range(len(d)):
 a=df.groupby('IMDB_Rating').get_group(d[i])
 b=len(a)
 accelerate.append(b)
plt.plot(d,accelerate)
plt.title('IMDB_Rating vs No_of_Votes')
plt.xlabel('IMDB_Rating')
plt.ylabel('No_of_Votes')
plt.show()



