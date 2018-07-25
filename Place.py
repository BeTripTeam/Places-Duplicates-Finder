class Point:
    def __init__(self, lat, lon):
        self.lattitude = lat
        self.longitude = lon


class Place:
    point = None
    names = []
    
    def __init__(self, point, name):
        self.point = point
        self.name = name
    
    def __repr__(self):
        return self.name