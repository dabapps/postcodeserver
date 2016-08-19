from flask import Flask, request, jsonify
import marisa_trie
import geohash


app = Flask(__name__)


db = marisa_trie.BytesTrie()
db.load('data/postcodes.marisa')


@app.route('/')
def lookup():
    if 'postcode' not in request.args:
        return jsonify(detail="Please supply a 'postcode' parameter", about="http://github.com/j4mie/postcodeserver"), 400
    try:
        postcode = request.args['postcode'].replace(' ', '').upper()
        hash = db[postcode][0].decode()
        lat, lng = geohash.decode(hash)
        return jsonify(postcode=postcode, geohash=hash, lat=lat, lng=lng)
    except:
        return jsonify(detail="Failed to lookup postcode"), 400


if __name__ == "__main__":
    app.run(debug=True)
