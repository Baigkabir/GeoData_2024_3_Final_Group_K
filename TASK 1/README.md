# Warming Stripes Task - Analysis and Visualization

This repository contains the solution for the "Warming Stripes" task, which involves the visualization of warming trends based on temperature data from stations in Baden-Württemberg, Germany.

## Task Overview

The task is divided into four sub-tasks:

1. **Sub-Task 1.1**: Selection of stations based on specific criteria.
2. **Sub-Task 1.2**: Creation of a geopackage layer and visualization in QGIS.
3. **Sub-Task 1.3**: Automation of temperature data download for the selected stations.
4. **Sub-Task 1.4**: Visualization of warming stripes using Seaborn.

---

## Sub-Task 1.1: Station Selection

### Objective:
Select stations that meet the following criteria:
- They are located in **Baden-Württemberg**.
- They are **still active**.
- Their records started **before 1950**.

### Solution:

In this sub-task, we first needed to filter the available stations based on the given criteria. The station data was read from the file [KL_Jahreswerte_Beschreibung_Stationen.txt](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/annual/kl/historical/KL_Jahreswerte_Beschreibung_Stationen.txt) which contains information about various weather stations in Germany.

Steps taken:
- **Step 1**: Loaded the station description file using Pandas.
- **Step 2**: Applied filters to select stations located specifically in the Baden-Württemberg region.
- **Step 3**: Further filtered the stations to include only those that are currently active and began recording data before 1950.
- **Step 4**: The filtered data was then saved in an Excel file `filtered_stations_Baden_Wurttemberg.xlsx`.

This resulted in a final set of 26 stations meeting the criteria, which were used in subsequent steps.

### Output:
- `filtered_stations_Baden_Wurttemberg.xlsx`: Contains the list of 26 filtered stations.

---

## Sub-Task 1.2: Geopackage Layer Creation and QGIS Visualization

### Objective:
- Use Geopandas to create a geopackage layer for the filtered stations.
- Load the geopackage into QGIS and visualize it with a topographic map as a background.
- Use **EPSG:25832** as the coordinate system and label the stations using their IDs and names.

### Solution:

This sub-task involved using **Geopandas** to create a spatial data layer that could be visualized in QGIS. The objective was to generate a map with station locations and relevant labels.

Steps taken:
- **Step 1**: Converted the filtered station data into a GeoDataFrame using Geopandas, which allowed us to handle geographic data.
- **Step 2**: Reprojected the data into the **EPSG:25832** coordinate system, which is commonly used for mapping in Europe, particularly in Germany.
- **Step 3**: Saved the stations as a **geopackage** file (`stations_BW.gpkg`), which contains geospatial data and is compatible with QGIS.
- **Step 4**: Opened the geopackage in QGIS and loaded the Baden-Württemberg WMS service as the base map.
- **Step 5**: Designed the map to include labels for each station, showing both the station name and ID for clarity.

This map helps visualize the spatial distribution of the selected stations across Baden-Württemberg and provides context for their geographic locations.

### Map:
![Map of Active Stations](Map%20(SubTask_1.2).png)

### Files:
- `stations_BW.gpkg`: The generated geopackage containing the filtered stations.
- `Geodata_SubTask_1_2.qgz`: QGIS project used to create the map.
- `Map (SubTask_1.2).png`: A visually designed map showing active stations in Baden-Württemberg.

---

## Sub-Task 1.3: Automating Data Download

### Objective:
- Automatically download the annual temperature data for the selected stations from the DWD historical KL data collection.

### Solution:

In this sub-task, the goal was to automate the process of downloading temperature data from the [DWD climate database](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/annual/kl/historical/) for the selected stations. Given the large dataset, manually downloading the data for each station would be inefficient, so automation was necessary.

Steps taken:
- **Step 1**: Established an FTP connection to the DWD open data portal where historical temperature data is stored.
- **Step 2**: Constructed a script that iterated over the list of selected station IDs (from Sub-Task 1.1) and downloaded the corresponding data files.
- **Step 3**: Each data file was saved locally, and the data was extracted and cleaned to ensure consistency.
- **Step 4**: The temperature data for all stations was then merged into a single dataset, which was ready for further analysis in Sub-Task 1.4.

The automated download process ensured that the temperature data for each station was fetched reliably, reducing the manual effort involved.

### Output:
- All temperature data for the selected stations was downloaded and merged into a single dataset for analysis.

---

## Sub-Task 1.4: Warming Stripes Visualization

### Objective:
- Plot warming stripes representing temperature deviations from the reference period (1971–2000) for the selected stations.
- The stripes will show the trend from 1950 to 2022, with blue indicating cooler years and red indicating warmer years.

### Solution:

In this final sub-task, we created a visualization known as **warming stripes**. This plot shows the temperature trends for the selected stations over time, relative to a reference period. The reference temperature is calculated as the average annual temperature between 1971 and 2000 for each station.

Steps taken:
- **Step 1**: For each station, we calculated the reference temperature by averaging the temperatures between 1971 and 2000.
- **Step 2**: Calculated the deviation of each year's temperature from the reference value. Positive deviations indicate warmer years (shown in red), and negative deviations indicate cooler years (shown in blue).
- **Step 3**: Used the Seaborn library to generate a **heatmap** where each stripe represents a year, and the color represents the deviation from the reference temperature.
- **Step 4**: The final plot visualizes warming and cooling trends for each station from 1950 to 2022, giving a clear picture of climate change in the region.

### Warming Stripes Plot:
![Warming Stripes Plot](Warming%20Strip%20Plot.png)

This visualization effectively shows the impact of global warming on local weather stations, with most stations showing increasing temperatures over time.

---

## How to Run the Project

1. **Jupyter Notebook**:
   - Open `GeoData_2024.ipynb` in Jupyter.
   - Follow the instructions in the notebook to reproduce the analysis and visualizations.

2. **QGIS**:
   - Open `Geodata_SubTask_1_2.qgz` in QGIS to visualize the stations and background topography.

3. **Warming Stripes Plot**:
   - Run the plotting code in the Jupyter notebook to generate the warming stripes plot for the selected stations.

---

## Additional Files
- `KL_Jahreswerte_Beschreibung_Stationen.xlsx`: Original station description file used for filtering.
- `stations_BW.gpkg`: Geopackage containing filtered stations.
- `Map (SubTask_1.2).png`: Map showing the selected stations in Baden-Württemberg.

---

## Summary

This project demonstrates how to work with geospatial data to analyze and visualize temperature trends. We used various Python libraries (Pandas, Geopandas, Seaborn) and QGIS to complete the tasks, ultimately producing a warming stripes plot similar to the one developed by Ed Hawkins.
