import csv
import sys
import geohash
import marisa_trie


def rebuild(filename):

    print("Rebuilding trie based on CSV file: %s" % filename)

    buffer = {}

    for row in csv.DictReader(open(filename)):
        try:
            postcode = row['Postcode'].replace('"', '').replace(' ', '').upper()
            lat = float(row['Latitude'])
            lon = float(row['Longitude'])
            hash = geohash.encode(lat, lon)
            buffer[str(postcode)] = hash.encode('utf-8')
        except:
            print('skipping %s' % row)

    trie = marisa_trie.BytesTrie(buffer.items())
    trie.save('data/postcodes.marisa')
    print("Done")


if __name__ == "__main__":
    filename = sys.argv[1]
    rebuild(filename)
