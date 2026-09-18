def total_active_area(parcels):
    """Q1: Total area of all active parcels"""
    return sum(p.area_sqm for p in parcels if p.is_active)


def parcels_above_threshold(parcels, threshold):
    """Q2: Parcels with area >= threshold"""
    return [p for p in parcels if p.area_sqm >= threshold]


def count_by_zone(parcels):
    """Q3: Count parcels per zone"""
    counts = {}
    for p in parcels:
        counts[p.zone] = counts.get(p.zone, 0) + 1
    return counts


def development_candidates(parcels, min_area, allowed_zones):
    """Q4: Development candidates (active, zone in allowed_zones, area >= min_area)"""
    return [
        p for p in parcels
        if p.is_active and p.zone in allowed_zones and p.area_sqm >= min_area
    ]


def intersecting_parcels(parcels, study_area):
    """Q5: Parcels intersecting a study-area polygon"""
    return [p for p in parcels if p.intersects(study_area)]


def suitable_cells(grid):
    """
    Q6: Return coordinates of cells that meet suitability criteria:
    slope <= max_slope_deg and flood <= max_flood_m
    """
    suitable = []
    max_slope = grid["criteria"]["max_slope_deg"]
    max_flood = grid["criteria"]["max_flood_m"]

    slope = grid["slope_deg"]
    flood = grid["flood_m"]

    for i in range(len(slope)):
        for j in range(len(slope[i])):
            s = slope[i][j]
            f = flood[i][j]
            if s is not None and f is not None:
                if s <= max_slope and f <= max_flood:
                    suitable.append((i, j))
    return suitable