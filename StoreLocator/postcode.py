import requests
from math import sin, cos, sqrt, atan2, radians

# Retrieves the coordinates from a given postcode
def coords(postcode):
    r = requests.get('https://api.postcodes.io/postcodes/' + postcode)
    response = r.json()
    print(response)
    if 'result' in response:
        print(response)
        return response['result']['longitude'], response['result']['latitude']

# Calculates the distance in km between two coordinates
def distance(lon1, lat1, lon2, lat2):
    radius = 6371

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = radius * c

    return distance

# Retrieves all stores within a given postcode and radius (km)
def search(stores, postcode, radius):

    results = []

    try:
        latitude, longitude = coords(postcode)
        for store in stores:

            if store['latitude'] and store['longitude']:
                dist = distance(radians(float(longitude)),
                                radians(float(latitude)),
                                radians(store['latitude']),
                                radians(store['longitude']))

                if dist < int(radius):
                    results.append(store)

    except Exception:
        pass

    return sorted(results, key=lambda x: x[3], reverse=True)
