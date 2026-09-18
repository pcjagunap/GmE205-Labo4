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

# Part C: Algorithm First

### Q1 – Total Active Area
Pseudocode:
SET total = 0  
FOR each parcel in parcels  
    IF parcel.is_active  
        ADD parcel.area_sqm to total  
RETURN total  

**Output:**  
Q1 Total Active Area: 597759.84  

---

### Q2 – Parcels Above Threshold
Pseudocode:
SET result = []  
FOR each parcel in parcels  
    IF parcel.area_sqm >= threshold  
        ADD parcel.id to result  
RETURN result  

**Output (threshold = 5000):**  
Q2 Parcels >= 5000: [1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 36, 39, 40, 41, 43, 44, 45, 47, 48, 49, 51, 54, 56, 57, 58, 62, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 78, 80, 83, 84, 85, 86, 87, 88, 89, 91, 94, 96, 97, 100]  

---

### Q3 – Zone Counts
Pseudocode:
SET counts = {}  
FOR each parcel in parcels  
    zone = parcel.zone  
    IF zone not in counts  
        SET counts[zone] = 0  
    INCREMENT counts[zone] by 1  
RETURN counts  

**Output:**  
Q3 Zone Counts: {'Industrial': 22, 'Residential': 49, 'Commercial': 29}  

---

### Q4 – Development Candidates
Pseudocode:
SET result = []  
FOR each parcel in parcels  
    IF parcel.is_active AND parcel.zone in [Residential, Commercial] AND parcel.area_sqm >= threshold  
        ADD parcel.id to result  
RETURN result  

**Output (min_area = 5000, zones = Residential + Commercial):**  
Q4 Development Candidates: [2, 5, 9, 10, 11, 14, 15, 16, 18, 22, 26, 28, 29, 32, 34, 39, 40, 41, 45, 47, 51, 54, 56, 57, 58, 65, 67, 68, 70, 71, 72, 73, 74, 75, 76, 78, 86, 87, 88, 89, 91, 94, 96, 97, 100]  

---

### Q5 – Parcels Intersecting Study Area
Pseudocode:
SET result = []  
FOR each parcel in parcels  
    IF parcel.geometry intersects study_area  
        ADD parcel.id to result  
RETURN result  

**Output (polygon around parcels (121.051, 14.658),(121.062, 14.658),(121.062, 14.664),(121.051, 14.664)):** 
Q5 Intersecting Parcels: [[1, 3, 22, 28, 45, 47, 54, 59, 61, 70, 77, 83]]  

---

### Q6 – Suitable Cells
Pseudocode:
SET result = []  
FOR each cell in grid  
    slope = slope_deg[i][j]  
    flood = flood_m[i][j]  
    IF slope <= max_slope_deg AND flood <= max_flood_m  
        ADD (i, j) to result  
RETURN result  

**Output (criteria: slope ≤ 15°, flood ≤ 0.5 m):**  
Q6 Suitable Cells: [(0, 0), (0, 3), (0, 4), (1, 0), (1, 4), (2, 1), (2, 2), (2, 4), (3, 0), (3, 1), (3, 3), (4, 1), (4, 2), (4, 4)]  
