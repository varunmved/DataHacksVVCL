import csv
import pdb

output = []
with open("sf-businesses.csv", "r") as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        latlong = row["Business_Location"].split("\n")[-1]
        latlong = latlong.replace("(", "").replace(")", "").replace(" ", "")
        coords = latlong.split(",")
        try:
            lat = float(coords[0])
            lng = float(coords[1])
            
            row["latitude"] = lat
            row["longitude"] = lng
            del row["Business_Location"]
            output.append(row)
        except Exception as e:
            continue

with open("cleaned-sf-businesses.csv", "w") as fout:
    writer = csv.DictWriter(fout, output[0].keys())
    writer.writeheader()
    writer.writerows(output)
