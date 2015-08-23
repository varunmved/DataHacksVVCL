import csv
import re
import datetime
import pdb

stups = open("dataSets/updatedSFStartups.csv", "r")
allbus = open("dataSets/cleaned-sf-businesses.csv", "r")
outfile = open("startup_matches.csv", 'w')

busReader = csv.DictReader(allbus)
all_companies = []
for row in busReader:
    all_companies.append(row)

all_startups = []
reader = csv.DictReader(stups)
for row in reader:
    all_startups.append(row)

results = []

for startup in all_startups:
    startup_name = startup["NAME"]
    founded_date = datetime.datetime.strptime(startup["FOUNDED_AT"], "%m/%d/%Y")
    
    total_found = 0
    matches = []
    for row in all_companies:
        company_name = row["business_name"]
        office_date = datetime.datetime.strptime(row["location_start_date"], "%m/%d/%Y")
        if re.match("^" + startup_name + "[^a-zA-Z0-9\-\,]", row["business_name"]) and\
                office_date >= founded_date:
            matches.append(row)
            print("%s -> %s" % (startup_name, row["business_name"]))
    
    if len(matches) >= 1 and len(matches) <= 3:
        results.extend(matches) 

writer = csv.DictWriter(outfile, results[0].keys())
writer.writeheader()
writer.writerows(results)
outfile.close()


print ("matches found: %s" % len(results))
outfile.close()
