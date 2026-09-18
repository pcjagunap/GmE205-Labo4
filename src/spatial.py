from shapely.geometry import shape

class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry

    def intersects(self, other):
        return self.geometry.intersects(other.geometry)

    def bbox(self):
        return self.geometry.bounds


class Parcel(SpatialObject):
    def __init__(self, parcel_id, geometry, attributes=None):
        super().__init__(geometry)
        self.id = parcel_id
        self.attributes = attributes or {}

    @property
    def area_sqm(self):
        return float(self.attributes["area_sqm"])

    @property
    def zone(self):
        return self.attributes["zone"]

    @property
    def is_active(self):
        return bool(self.attributes["is_active"])

    @classmethod
    def from_dict(cls, record):
        geom = shape(record["geometry"])
        attributes = {
            "zone": record["zone"],
            "is_active": record["is_active"],
            "area_sqm": record["area_sqm"],
        }
        return cls(record["parcel_id"], geom, attributes)

    def __repr__(self):
        return f"Parcel(id={self.id}, zone={self.zone}, active={self.is_active}, area={self.area_sqm})"