# LABORATORY 4 - Spatial Algorithms and Structured Programming

'''text
    Lab4/
    ├── data/                
    │   ├── parcels.json
    │   └── suitability_grid.json
    ├── output/              
    ├── src/                 
    │   ├── spatial.py
    │   ├── analysis.py
    │   ├── demo.py
    │   └── run_lab4.py
    ├── tests/               
    │   ├── test_spatial.py
    │   └── test_analysis.py
    ├── README.md
    ├── requirements.txt
    └── .gitignore
'''

# Part A: Project Setup and Reproducible Workspace

- Created folder with subdirectories: `data/`, `src/`, `tests/`, `output/`.
- Initialized Python virtual environment `.venv`.
- Installed dependencies: shapely, matplotlib.
- Added `.gitignore` to exclude `output/` and `.venv`.
- Initialized Git repository and pushed first commit.

# Part B: Carry Forward Object Model

- Reused `SpatialObject` and `Parcel` classes from Laboratory 3.
- `Parcel` now includes `@property` methods for `area_sqm`, `zone`, and `is_active`.
- Added `from_dict()` constructor to build Parcel objects directly from JSON records.
- Verified with demo record:
  - parcel_id: 1
  - zone: Industrial
  - is_active: True
  - area_sqm: 5871.15
- Demo script confirms properties return correct values and geometry is handled by Shapely

# Laboratory 4 – Part C: Algorithm First

### Q1 – Total Active Area
Pseudocode:
SET total = 0  
FOR each parcel in parcels  
    IF parcel.is_active  
        ADD parcel.area_sqm to total  
RETURN total

### Q2 – Parcels Above Threshold
Pseudocode:
SET result = []  
FOR each parcel in parcels  
    IF parcel.area_sqm >= threshold  
        ADD parcel.id to result  
RETURN result  

### Q3 – Zone Counts
Pseudocode:
SET counts = {}  
FOR each parcel in parcels  
    zone = parcel.zone  
    IF zone not in counts  
        SET counts[zone] = 0  
    INCREMENT counts[zone] by 1  
RETURN counts

### Q4 – Development Candidates
Pseudocode:
SET result = []  
FOR each parcel in parcels  
    IF parcel.is_active AND parcel.zone in [Residential, Commercial] AND parcel.area_sqm >= threshold  
        ADD parcel.id to result  
RETURN result

### Q5 – Parcels Intersecting Study Area
Pseudocode:
SET result = []  
FOR each parcel in parcels  
    IF parcel.geometry intersects study_area  
        ADD parcel.id to result  
RETURN result