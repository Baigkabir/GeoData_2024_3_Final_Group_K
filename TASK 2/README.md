# Task 2: Digitization - Burial Mounds in Uedemer Hochwald

This task involves the georeferencing, terrain analysis, and digitization of historical burial mounds located in the Uedemer Hochwald forest, utilizing QGIS and geospatial tools.

## Sub-Tasks Overview:
1. **Sub-Task 2.1**: Georeferencing a historical map of the burial mounds.
2. **Sub-Task 2.2**: Creating and analyzing a hillshade model.
3. **Sub-Task 2.3**: Measuring the elevation of burial mounds relative to their surroundings.
4. **Sub-Task 2.4**: Identifying and digitizing rectangular structures in the terrain.

---

## Sub-Task 2.1: Georeferencing the Burial Mounds Map

### Objective:
Georeference a historical map of burial mounds using QGIS and the DTK10 NRW topographic map. Ensure accuracy by identifying ground control points (GCPs) from identifiable landmarks and roads, and use the EPSG:25832 projection.

### Solution:
- **Step 1**: Loaded the historical burial mounds map into QGIS.
- **Step 2**: Identified control points (forest trails, roads, and junctions) that are clearly visible both on the map and on the DTK10 topographic layer.
- **Step 3**: Used QGIS’s Georeferencer tool to align the burial mounds map to real-world coordinates. Added the georeferenced map back to the project with EPSG:25832 projection.

### Explanation of Map:
The georeferenced map was aligned based on visible landmarks such as roads and trails. These control points ensured that the burial mounds could be accurately placed on modern maps. The map clearly shows the ancient burial mounds within their surrounding terrain.

### Files:
- `Burial_Mounds_Georeferenced.tif`: The georeferenced map of the burial mounds.
- `GEOREFERENCING POINTS.points`: Ground control points used for the georeferencing process.
- `SUBTASK_2.1_Burial_Mounds_Uedem_V001.qgz`: The QGIS project file with the georeferenced map.

### Visualization:
#### GEOREFERENCER TOOL:
![GEOREFERENCER TOOL](SUBTASK%202.1/SUBTASK_2.1_IMG1%20(GEOREFERENCER%20TOOL).png)

#### GEOREFERENCE WITH DTK10 MAP:
![GEOREFERENCE WITH DTK10 MAP](SUBTASK%202.1/SUBTASK_2.1_IMG2%20(GEOREFERENCE%20WITH%20DTK10%20MAP).png)

#### Final Layout of Georeferenced Map and Points of Reference:
![Final Layout of Georeferenced Map](SUBTASK%202.1/SUBTASK_2.1%20(Final%20layout%20of%20georefrenced%20map%20and%20points%20of%20reference%20).png)


### Judgement:
The georeferencing process was highly accurate, as confirmed by the proper alignment of key landmarks like crossroads and forest trails. This ensures that further analyses of the burial mounds are based on reliable geospatial data.

---

## Sub-Task 2.2: Hillshade Model Creation and Map Comparison

### Objective:
Create a hillshade model from the Digital Terrain Model (DTM) and overlay the georeferenced burial mounds map. Compare how well the burial mounds are represented in the terrain.

### Solution:
- **Step 1**: Created a hillshade model from the DTM layer using QGIS.
- **Step 2**: Overlaid the georeferenced burial mounds map onto the hillshade model. The burial mounds map was made semi-transparent for better visual comparison with the terrain.
- **Step 3**: Analyzed the burial mound positions in relation to the topography visible in the hillshade model.

### Explanation of Map:
The hillshade model reveals subtle variations in terrain elevation, highlighting the burial mounds as raised features. By comparing the georeferenced map and the hillshade model, we can verify that the burial mounds correspond to elevated terrain, confirming their accurate geolocation.

### Files:
- `hillshade_model.tif`: The hillshade model generated from the DTM layer.
- `SUBTASK_2.2_Burial_Mounds_Uedem_V001.qgz`: The QGIS project file for Sub-Task 2.2, containing the hillshade model and the georeferenced map.
- `GEOREFERENCE MAP WITH BURIAL MOUNDS (SUBTASK 2.2 MAP 1).png`, `GEOREFERENCE MAP WITH BURIAL MOUNDS (SUBTASK 2.2 MAP 2).png`, `GEOREFERENCE MAP WITH BURIAL MOUNDS (SUBTASK 2.2 MAP 3).png`: Images showing the map overlay with the hillshade model.

### Visualization:

#### Georeferenced Map with Burial Mounds Overlay on Hillshade Model:
![Georeferenced Map with Burial Mounds](SUBTASK%202.2/GEOREFERENCE%20MAP%20WITH%20BURIAL%20MOUNDS%20(SUBTASK%202.2%20MAP%201).png)

#### Georeferenced Map with Burial Mounds Overlay on Hillshade Model:
![Georeferenced Map with Burial Mounds](SUBTASK%202.2/GEOREFERENCE%20MAP%20WITH%20BURIAL%20MOUNDS%20(SUBTASK%202.2%20MAP%202).png)

#### Georeferenced Map with Burial Mounds Overlay on Hillshade Model:
![Georeferenced Map with Burial Mounds](SUBTASK%202.2/GEOREFERENCE%20MAP%20WITH%20BURIAL%20MOUNDS%20(SUBTASK%202.2%20MAP%203).png)

### Judgement:
The burial mounds appear prominently in the hillshade model, indicating that the mounds were properly georeferenced in Sub-Task 2.1. The comparison with the terrain demonstrates that these mounds correspond to real topographical features.

---

## Sub-Task 2.3: Measuring Mound Heights Relative to Their Environment

### Objective:
Measure the typical height of burial mounds relative to their direct environment, using the DTM layer to calculate elevation differences.

### Solution:
- **Step 1**: Used the Profile Tool in QGIS to draw lines across the burial mounds and measure the elevation profiles.
- **Step 2**: Recorded and analyzed the elevation profiles to calculate the relative heights of the mounds compared to their surroundings.
- **Step 3**: Visualized the elevation profiles in graphs for better understanding of the height variations.

### Explanation of Graphs:
The elevation profiles show a typical height difference of around 1 to 2 meters between the mounds and their surrounding environment. These elevation changes are significant in a relatively flat landscape, highlighting the importance of the burial mounds.

### Files:
- `Burial_mounds_elevation_from_direct_environment (ELEVATION MEASUREMENT 1).xlsx`, `Burial_mounds_elevation_from_direct_environment (ELEVATION MEASUREMENT 2).xlsx`, `Burial_mounds_elevation_from_direct_environment (ELEVATION MEASUREMENT 3).xlsx`: Elevation data recorded from the burial mound profiles.
- `ELEVATION MEASUREMENT GRAPH_1.png`, `ELEVATION MEASUREMENT GRAPH_2.png`, `ELEVATION MEASUREMENT GRAPH_3.png`: Graphs showing the elevation profiles of the burial mounds.
- `SUBTASK_2.3_Burial_Mounds_Uedem_V001.qgz`: The QGIS project used for elevation measurements.

### Visualization:

#### Elevation Profile Graph 1:
![Elevation Measurement 1](SUBTASK%202.3/ELEVATION%20MEASUREMENT%20GRAPH_1.png)

#### Elevation Profile Graph 2:
![Elevation Measurement 2](SUBTASK%202.3/ELEVATION%20MEASUREMENT%20GRAPH_2.png)

#### Elevation Profile Graph 3:
![Elevation Measurement 2](SUBTASK%202.3/ELEVATION%20MEASUREMENT%20GRAPH_3.png)

### Judgement:
The elevation differences measured between the mounds and their surrounding environment confirm that these structures were intentionally raised, likely for ceremonial or burial purposes. The mounds are distinct, man-made features in the landscape.

---

## Sub-Task 2.4: Identifying and Digitizing Rectangular Structures

### Objective:
Identify weakly visible rectangular structures to the East-North-East of the burial mounds area in the hillshade model and digitize them using polygons.

### Solution:
- **Step 1**: Analyzed the hillshade model to locate faint rectangular patterns, likely remnants of ancient structures or terrain modifications.
- **Step 2**: Digitized these structures in QGIS by creating polygons around the visible patterns.
- **Step 3**: Saved the digitized structures in a geopackage for further analysis or visualization.

### Explanation of Map:
The rectangular structures identified in the hillshade model suggest possible man-made formations or remnants of ancient settlements. These structures do not follow natural terrain contours, indicating human activity. 

### Files:
- `Rectangular_Structures.gpkg`, `Rectengular_structure_2.gpkg`: Geopackages containing the digitized rectangular structures.
- `SUBTASK_2.4_Burial_Mounds_Uedem_V001.qgz`: The QGIS project for digitizing rectangular structures.
- `Digitization of rectangular structures in ENE direction (IMG 1).png`, `Digitization of rectangular structures in ENE direction (IMG 2).png`: Images showing the digitized rectangular structures.

### Visualization:

#### Digitized Rectangular Structures in the ENE Direction:
![Digitized Rectangular Structures](SUBTASK%202.4/Digitization%20of%20rectangular%20structures%20in%20ENE%20direction%20(IMG%201).png)

#### Digitized Rectangular Structures in the ENE Direction:
![Digitized Rectangular Structures 1](SUBTASK%202.4/Digitization%20of%20rectangular%20structures%20in%20ENE%20direction%20(IMG%202).png)

### Judgement:
These rectangular structures are likely ancient remains of settlements or enclosures. Their size and alignment suggest purposeful human construction, rather than natural terrain formations.

---

## How to Run the Project:

1. **Open the QGIS Project Files**: Each sub-task has its own QGIS project file that contains the necessary layers (e.g., DTM, hillshade model, georeferenced map, and digitized structures). Open the project files to view and explore the data.
   - For example, use `SUBTASK_2.1_Burial_Mounds_Uedem_V001.qgz` for Sub-Task 2.1, etc.
   
2. **Analyze the Geospatial Data**: Use the provided georeferenced maps, hillshade models, and elevation measurements to study the burial mounds and their surrounding terrain.

3. **Review the Graphs**: The elevation measurement graphs provide a detailed analysis of the mound heights relative to their environment.

4. **Examine the Digitized Structures**: The rectangular structures have been digitized in QGIS, and the corresponding geop
