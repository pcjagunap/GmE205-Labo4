import os, json
from shapely.geometry import shape, Polygon
from spatial import Parcel
from analysis import (
    total_active_area,
    parcels_above_threshold,
    count_by_zone,
    development_candidates,
    intersecting_parcels,
    suitable_cells
)

def load_parcels():
    """Load parcels from JSON into Parcel objects"""
    base = os.path.dirname(__file__)
    path = os.path.join(base, "..", "data", "parcels_shapely_ready.json")
    with open(path) as f:
        data = json.load(f)
    return [Parcel.from_dict(r) for r in data]

def demo():
    parcels = load_parcels()

    # Q1
    print("Q1 Total Active Area:", total_active_area(parcels))

    # Q2
    print("Q2 Parcels >= 5000:", [p.id for p in parcels_above_threshold(parcels, 5000)])

    # Q3
    print("Q3 Zone Counts:", count_by_zone(parcels))

    # Q4
    print("Q4 Development Candidates:",
          [p.id for p in development_candidates(parcels, 5000, ["Residential", "Commercial"])])

    # Q5
    study_area_path = os.path.join(os.path.dirname(__file__), "..", "data", "study_area.json")
    if os.path.exists(study_area_path):
        with open(study_area_path) as f:
            study_area = shape(json.load(f))
        print("Q5 Intersecting Parcels:",
              [p.id for p in intersecting_parcels(parcels, study_area)])
    else:
        
        study_area = Polygon([
    (121.051, 14.658),
    (121.062, 14.658),
    (121.062, 14.664),
    (121.051, 14.664)
    ])
        print("Q5 Intersecting Parcels (demo polygon):",
              [p.id for p in intersecting_parcels(parcels, study_area)])

    # Q6
    grid_path = os.path.join(os.path.dirname(__file__), "..", "data", "suitability_grid.json")
    if os.path.exists(grid_path):
        with open(grid_path) as f:
            grid = json.load(f)
        print("Q6 Suitable Cells:", suitable_cells(grid))
    else:
        print("Q6 skipped: suitability_grid.json not found")

if __name__ == "__main__":
    demo()
