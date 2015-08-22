import csv
import pdb

stups = open("dataSets/sfStartupsAllCaps.txt", "r")
allbus = open("dataSets/cleaned-sf-businesses.csv", "r")
outfile = open("test.csv", 'w')
i = 0


busReader = csv.DictReader(allbus)
a = csv.writer(outfile, delimiter=',')
for rowStups in stups:
    startup_name = rowStups.strip()
    #print startup_name
    if startup_name == "TWILIO":
        print("yup!")
    for row in busReader:
        if  "TWILIO" in row["business_name"]:
            print ("yee!")
        #print(rowStups)
        #print(row["business_name"])
        if str(startup_name) in (row["business_name"]).strip():
            i +=1
            print("%s -> %s" % (startup_name, row["business_name"]))
            # outText = [row[2],row[9],row[1], row[3]]
            #a.writerows(outText)

print(i)
outfile.close()
