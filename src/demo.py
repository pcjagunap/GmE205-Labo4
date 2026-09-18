from spatial import Parcel

def demo_parcel():
    record = {
        "parcel_id": 1,
        "zone": "Industrial",
        "is_active": True,
        "area_sqm": 5871.15,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [[121.05, 14.65], [121.06, 14.65], [121.06, 14.66], [121.05, 14.66], [121.05, 14.65]]
            ]
        }
    }

    parcel = Parcel.from_dict(record)
    print(parcel)

if __name__ == "__main__":
    demo_parcel()