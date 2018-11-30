postcodes
=========

A tiny JSON server for getting the latitude and longitude of a UK postcode.

You can see it running at [postcodes.herokuapp.com/?postcode=bn11ag](http://postcodes.herokuapp.com/?postcode=bn11ag).

Created by [Jamie Matthews](http://dabapps.com/community/people/jamie-matthews/). Follow me on Twitter: [@j4mie](https://twitter.com/j4mie)

running locally
---------------

    git clone git@github.com:j4mie/postcodeserver.git
    cd postcodeserver
    python3 -m venv env
    env/bin/pip install -r requirements.txt
    env/bin/python server.py

using from another program
--------------------------

```pycon
>>> import requests
>>> requests.get('http://postcodes.herokuapp.com', params={'postcode': 'BN1 1AG'}).json()
{u'lat': 50.82292196340859, u'lng': -0.14287104830145836, u'geohash': u'gcpchspbyz7d', u'postcode': u'BN11AG'}
```

data source
-----------

Loaded with data from [here](http://www.doogal.co.uk/UKPostcodes.php). The original source is the [Ordnance Survey Code-Point Open](http://www.ordnancesurvey.co.uk/oswebsite/products/code-point-open/).

rebuilding the trie
-------------------

The repository includes the postcode database encoded using [marisa-trie](https://github.com/kmike/marisa-trie) (the resulting file is approx. 19 MB). To rebuild this, you'll need a CSV file with at least three columns: postcode, latitude, longitude. The file linked above (under Data Source) matches this format:

    $ head -5 postcodes.csv 
    Postcode,Latitude,Longitude,Easting,Northing,GridRef,County,District,Ward,DistrictCode,WardCode,Country,CountyCode
    AB10 1AA,57.148235,-2.096648,394251,806376,NJ942063,"","Aberdeen City","George St/Harbour Ward", S12000033,S13002483,Scotland,
    AB10 1AB,57.149079,-2.096964,394232,806470,NJ942064,"","Aberdeen City","George St/Harbour Ward", S12000033,S13002483,Scotland,
    AB10 1AF,57.14871,-2.097806,394181,806429,NJ941064,"","Aberdeen City","George St/Harbour Ward", S12000033,S13002483,Scotland,
    AB10 1AG,57.148235,-2.096648,394251,806376,NJ942063,"","Aberdeen City","George St/Harbour Ward", S12000033,S13002483,Scotland,

To import this file, run `env/bin/python rebuild.py path/to/postcodes.csv`

disclaimer
----------

It goes without saying that this software (and the service running on Heroku) comes with no warranties or guarantees to its accuracy, availability or stability. Use at your own risk.

code license
------------

[unlicense.org](http://unlicense.org/)

## Code of conduct

For guidelines regarding the code of conduct when contributing to this repository please review [https://www.dabapps.com/open-source/code-of-conduct/](https://www.dabapps.com/open-source/code-of-conduct/)

