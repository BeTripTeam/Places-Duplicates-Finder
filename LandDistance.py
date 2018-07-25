from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return km


def dis_eval(place, p):
    d = haversine(place.point.lattitude, place.point.longitude, p.point.lattitude, p.point.longitude)
    return 1 if abs(d)<=2 else abs(d)/2 + 1


def land_distance_sort(place, places):
    for p in places:
        pass
    return sorted([(p, dis_eval(place, p)) for p in places], key=lambda x: x[1])

