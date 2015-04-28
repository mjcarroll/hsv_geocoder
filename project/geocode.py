from pygeocoder import Geocoder, GeocoderError

from project.models import Location
import json

class GeocodeCache(object):
    def __init__(self, db):
        self.db = db

    def geocode(self, address_string):
        data = Location.query.filter(Location.search_street == address_string).first()

        if not data:
            try:
                result = Geocoder.geocode(address_string)
            except GeocoderError:
                result = None

            if result:
                data = Location(address_string)
                data.valid_address = result.valid_address
                data.full_address = result.full_address
                data.country = result.country
                data.postal_code = result.postal_code
                data.locality = result.locality
                data.street = result.route
                data.number = result.street_number
                data.lat, data.lng = result.coordinates
                data.raw = json.dumps(result.raw)
                self.db.session.add(data)
                self.db.session.commit()

        print data.raw
        dd = {}
        dd['valid_address'] = data.valid_address
        dd['full_address'] = data.full_address
        dd['country'] = data.country
        dd['postal_code'] = data.postal_code
        dd['locality'] = data.locality
        dd['street'] = data.street
        dd['number'] = data.number
        dd['lat'] = data.lat
        dd['lng'] = data.lng
        dd['raw'] = json.loads(data.raw)
        return dd