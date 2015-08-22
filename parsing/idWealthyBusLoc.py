import csv

with open('sfBuss.csv', 'rb') as csvfile:
   busReader = csv.reader(csvfile)
   for row in busReader:
       if "COFFEE" in row[3] and "San Francisco" in row[5]:
           print row[3]
           print row[5]
