from flask import Flask, Response, request, abort
import marisa_trie
import geohash
import json


app = Flask(__name__)

db = marisa_trie.BytesTrie()
db.load('data/postcodes.marisa')


@app.route('/')
def lookup():
    try:
        postcode = request.args['postcode'].replace(' ', '').upper()
        hash = db[postcode][0]
        lat, lng = geohash.decode(hash)
        data = json.dumps({'postcode': postcode, 'geohash': hash, 'lat': lat, 'lng': lng})
        return Response(data, mimetype='application/json')
    except:
        abort(404)


if __name__ == "__main__":
    app.run()
