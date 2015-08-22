import shapefile
import pprint
import sys
import pdb

pp = pprint.PrettyPrinter(indent=2, width=100)

if len(sys.argv) != 2:
    print("usage: python shp2json.py /path/to/shp/file")
else:
    filepath = sys.argv[1]
    sf = shapefile.Reader(filepath)
    pp.pprint(sf.fields)
    pp.pprint(sf.records()[51])

