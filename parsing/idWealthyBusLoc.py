import csv

def fancyFinder(row):
    if "COFFEE" in row[3] or "STARBUCKS" in row[3] or "CROSSFIT" in row[3] or "WHOLE FOODS" in row[3] or "TRADER JOE'S" in row[3]:
        return True

def extractAdd(row):
    strIn = row[16]
    str2 = strIn.split("(")
    add = str2[0]
    addLen = len(add)
    add = add[0:addLen-1]
    str3 = str2[1].split(",")
    lat = str3[0]
    longt = str3[1]
    longt = longt.strip()
    longtLen = len(longt)
    longt = longt[0:longtLen-1]
    #print(add + '\t' + lat + '\t' + longt)
    return add,lat,longt

file = open("fancyPlaces2.txt", "w")
with open('dataSets/sfBuss.csv', 'rb') as csvfile:
   busReader = csv.reader(csvfile)
   for row in busReader:
       if "San Francisco" in row[5]:
           if fancyFinder(row) == True:
               (add,lat,longt) = extractAdd(row)
               file.write(add)
               #file.write(row[3])

file.close()
