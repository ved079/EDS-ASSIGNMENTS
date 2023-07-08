import csv
file=open('Sales.csv','r')
data1=list(csv.reader(file,delimiter=','))
file.close()
print(data1)
f1 = open("Sales.csv","r")
data = list(csv.reader(f1))
CName = []; CGender = [] ; CCity = []
Product = {}
SName = () ; SCity = ()
l1 = []; l2 = []
for i in range(1,len(data)):
    pd = []
    print(data[i])

CName.append(data[i][0])
CGender.append(data[i][1])
CCity.append(data[i][2])
pd.append(data[i][3])
pd.append(data[i][3])
pd.append(data[i][3])
pd.append(data[i][3])
print(pd)
Product [data[i][3]] = pd
l1.append(data[i][3])
l2.append(data[i][3])
SName = tuple(l1)
SCity = tuple(l2)
print(CName)
print(CGender)
print(CCity)
for k in Product.keys():
    print(k , Product[k])
    print(SName)
    print(SCity)
Male=0
Female=0
for i in range(1,len(data)):
    if data[i][2]=='Male':
        Male=Male+1
    else:
        Female=Female+1
        print('No. of Males=', Male)
        print('No. of Females=', Female)
max=''
key_i=0
i=0
for i in range(1,len(data)):
    if(max<(data[i][2])):
        max = (data[i][2])
        key_i = i
        max = max + 1
        print('Best Supplier=', max)
