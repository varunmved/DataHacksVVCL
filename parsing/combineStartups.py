import csv
import re
import datetime

stups = open("dataSets/updatedSFStartups.csv", "r")
allbus = open("dataSets/cleaned-sf-businesses.csv", "r")
outfile = open("test.csv", 'w')
matches = 0

busReader = csv.DictReader(allbus)
all_companies = []
for row in busReader:
    all_companies.append(row)

all_startups = []
reader = csv.DictReader(stups)
for row in reader:
    all_statups.append(row)

a = csv.writer(outfile, delimiter=',')
for startup in all_startups:
    startup_name = rowStups.strip()
    for row in all_companies:
        #print(rowStups)
        #print(row["business_name"])
        if re.match("^" + startup_name + "[^a-zA-Z0-9]", row["business_name"]):
        # if str(startup_name) in (row["business_name"]).strip():
            matches += 1
            print("%s -> %s" % (startup_name, row["business_name"]))
            # outText = [row[2],row[9],row[1], row[3]]
            #a.writerows(outText)

print("matches: %s" % matches)
outfile.close()
