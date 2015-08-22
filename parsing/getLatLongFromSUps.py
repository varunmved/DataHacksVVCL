import geocoder

fileN = open("newfile2.txt", "w")

with open('dataSets/sfStartups.txt') as f:
    for line in f:
        lineL = line.strip() + ' near San Francisco'
        g = geocoder.google(lineL)
        res = str(g.latlng)
        #print(lineL)
        fileN.write(line.strip() + ' ' + res + '\n')
