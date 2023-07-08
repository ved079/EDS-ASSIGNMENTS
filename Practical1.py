import csv
file2 = open("PLACEMENT.csv", 'r')
file1 = open("RESULT.csv", 'r')
file3 = open("student.txt", 'r')
listcurrent = []
for i in file1:
 print(i)
print("____________________________________________________")
for i in file2:
 print(i)
print("____________________________________________________")
for i in file3:
 print(i)
print("____________________________________________________")
file2.close()
file1.close()
file3.close()
file2 = open("PLACEMENT.csv", 'r')
file1 = open("RESULT.csv", 'r')
file3 = open("student.txt", 'r')
data1 = list(csv.reader(file1, delimiter=','))
data2 = list(csv.reader(file2, delimiter=','))
data3 = list(csv.reader(file3, delimiter=','))
for i in range(5):
 listcurrent.append(data1[i] + data2[i] + data3[i])
for i in listcurrent:
 print(i)
print("____________________________________________________")
b = len(listcurrent)
listsal = []
for i in range(1, b, 1):
 listsal.append(int(listcurrent[i][2]))
listsal.sort()
print("stored value are", listsal)
print("the highest marks in sub 1 = ", max(listsal))
print("the lowest marks in sub 1 = ", min(listsal))
m = sum(listsal) / len(listsal)
print("the average marks in sub1 = ", m)
print("____________________________________________________")
file2.close()
file1.close()
for i in range(1, b, 1):
 listsal.append(int(listcurrent[i][3]))
listsal.sort()
print("stored value are", listsal)
print("the highest marks in sub 2 = ", max(listsal))
print("the lowest marks in sub 2 = ", min(listsal))
m = sum(listsal) / len(listsal)
print("the average marks in sub 2 = ", m)
print("____________________________________________________")
file2.close()
