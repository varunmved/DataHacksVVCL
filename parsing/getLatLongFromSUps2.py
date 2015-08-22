import geopy
import pdb

fileN = open("newfile2.txt", "w")

with open('dataSets/sfStartups.txt') as f:
    lines = f.readlines()
    for line in lines[0:10]:
    # for line in f:
        lineL = line.strip()
        geolocator = geopy.geocoders.GoogleV3()
        location = geolocator.geocode(lineL)
        if location:
            lat = location.latitude
            lng = location.longitude
            # bounding box of SF
            # -122.517187,37.730394,-122.381473,37.809787
            print("%s -> %s, %s" % (lineL, lat, lng))
            if (lat >= 37.730394 and lat <= 37.809787) and (lng >= -122.381473 and lng <= -122.517187):
                fileN.write("%s, %s, %s\n" % (lineL, lat, lng))
