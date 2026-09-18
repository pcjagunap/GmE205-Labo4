from shapely.geometry import shape

class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry

    def bbox(self):
        return self.geometry.bounds

    def intersects(self, other):
        """
        Check intersection with either another SpatialObject/Parcel
        or directly with a Shapely geometry (Polygon, Point, etc.).
        """
        if hasattr(other, "geometry"):
            return self.geometry.intersects(other.geometry)
        else:
            return self.geometry.intersects(other)


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
        geometry = shape(record["geometry"])
        attributes = {
            "zone": record["zone"],
            "is_active": record["is_active"],
            "area_sqm": record["area_sqm"],
        }
        return cls(record["parcel_id"], geometry, attributes)
