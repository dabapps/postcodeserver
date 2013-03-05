import sys
import geohash
import marisa_trie


def rebuild(filename):

    print "Rebuilding trie based on CSV file: %s" % filename

    buffer = {}

    for line in open(filename):
        try:
            parts = line.strip().split(',')
            postcode = parts[0].replace('"', '').replace(' ', '').upper()
            lat = float(parts[1])
            lon = float(parts[2])
            hash = geohash.encode(lat, lon)
            buffer[unicode(postcode)] = hash
        except:
            print 'skipping %s' % line

    trie = marisa_trie.BytesTrie(buffer.iteritems())
    trie.save('data/postcodes.marisa')
    print "Done"


if __name__ == "__main__":
    filename = sys.argv[1]
    rebuild(filename)
