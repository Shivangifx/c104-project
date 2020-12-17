from collections import Counter
import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][2]
	new_data.append(n_num)

def mode():
    data = Counter(new_data)
    oc = 0
    he = 0
    for hi, o in data.items():
        if o >= oc :
                oc = o
                he = hi
    print("Mode is : ",he)  


def mean():
    n = len(new_data)
    total =0
    for x in new_data:
        total += float(x)
    mean = total / n
    print("Mean / Average is: " + str(mean))



def median():
    n = len(new_data)
    new_data.sort()

    if n % 2 == 0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2 - 1])
        median = (median1 + median2)/2
    else:
        median = new_data[n//2]
    print("Median is: " + str(median))
    
mean()
median()
mode()
