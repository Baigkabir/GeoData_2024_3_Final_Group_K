# Task 3: OpenHygrisC Nitrate Data - Create a Movie with the QGIS Temporal Controller

## Overview:

The goal of this task is to visualize the changes in nitrate concentrations over time using **OpenHygrisC** data stored in a **PostgreSQL/PostGIS** geodatabase. The temporal animation is created using **QGIS Temporal Controller**, and the output is a movie that displays the nitrate levels from the earliest available measurements in the 1960s up to the most recent in the 2020s.

---

## Step-by-Step Solution:

### 1. **Setting Up the OpenHyPE System**

#### Objective:
We first set up the **OpenHyPE system**, which involves linking QGIS to a live PostgreSQL/PostGIS geodatabase containing the nitrate data and other relevant spatial information. 

#### Solution:
- **Step 1**: We initialized a **PostgreSQL** database with **PostGIS** extension enabled.
- **Step 2**: The following SQL scripts were executed to create the required users and database for handling the environmental data:
    - `010_create_users_for_env_db_V001.sql` – This creates the users needed for the PostgreSQL setup.
    - `020_create_database_env_db_V001.sql` – This creates the actual environmental database where data will be stored.
- **Step 3**: The nitrate data and station locations were then imported into the PostgreSQL/PostGIS database using provided Python notebooks.

### 2. **Importing Nitrate Data**

#### Objective:
We imported the **OpenHygrisC nitrate concentration data** along with relevant geospatial information (stations, measurement data) into the **PostgreSQL** database, and prepared this data for use in **QGIS**.

#### Solution:
- **Step 1**: Several datasets were imported into the database using the following Jupyter notebooks:
    - `import_messstelle.ipynb`: Imported data related to the groundwater measurement stations.
    - `import_katalog_stoff.ipynb`: Imported the catalog of substances, including nitrate, for which measurements are recorded.
    - `import_messwert.ipynb`: Imported the actual nitrate measurement data.
- **Step 2**: After importing the data, the **shapefiles** needed for QGIS visualization were generated using the following scripts:
    - `Generate_shape_files.ipynb` and `shape_file_nitrat.ipynb` were used to create shapefiles containing nitrate concentration data at different points in time.
- **Step 3**: The data was processed into **geopackage** files (`nitrat_local.gpkg`), which were used in the final QGIS project.

### 3. **Using the QGIS Temporal Controller**

#### Objective:
Using the **QGIS Temporal Controller**, we visualized the temporal changes in nitrate concentrations, starting from the earliest measurements in the 1960s up to the latest available data in the 2020s. The data was exported as images at regular time intervals and compiled into a video.

#### Solution:
- **Step 1**: Loaded the **Geodata_Task_3.qgz** project into QGIS. This project contains all the necessary layers, including the nitrate concentrations.
- **Step 2**: Configured the **Temporal Controller** in QGIS to animate the nitrate data over time. The time range was set to cover the years from the 1960s to the 2020s.
- **Step 3**: Instead of manually controlling the temporal slider, we exported images at specific intervals, allowing the nitrate data for each year to be captured.
- **Step 4**: These exported images were then compiled into a video using a video editing tool to produce the final nitrate concentration animation.

### Explanation of the Temporal Visualization:
The animation shows how nitrate levels in groundwater have evolved over the decades, highlighting changes in different regions. The concentration levels are represented with distinct color codes, making it easy to observe trends in nitrate pollution.

### Explanation from the Task:
In the question, we were asked to observe the time-varying nitrate concentration data. The temporal analysis shows increasing nitrate concentration levels in many areas, particularly in agricultural regions, reflecting the effects of fertilizer use and other industrial activities. This visualization highlights the importance of monitoring groundwater quality over time.

---

## Final Video and GIF Animation

### Visualization:
The nitrate concentration data has been visualized as a GIF below, showing changes from the earliest measurements to the most recent ones.

#### Nitrate Concentration Levels Animation:
![Nitrate Concentration Animation](Map%20Animation.gif)

### Files:
- `Geodata_Task_3.qgz`: The QGIS project file used to set up the temporal controller for nitrate concentration data.
- `Map Animation.mp4`: The final video output showing the temporal change in nitrate concentration.
- `Map Animationn.gif`: A GIF version of the temporal nitrate concentration animation.

---

## How to Run the Project:

### Requirements:
- **PostgreSQL** with **PostGIS** extension
- **QGIS** with **Temporal Controller** plugin enabled

### Steps:
1. **Set Up the Database**:
   - Run the SQL scripts to create users and set up the environmental database.
     - `010_create_users_for_env_db_V001.sql`
     - `020_create_database_env_db_V001.sql`
   
2. **Import the Data**:
   - Use the Jupyter notebooks to import the relevant datasets:
     - `import_messstelle.ipynb` for stations
     - `import_messwert.ipynb` for nitrate data
     - `import_katalog_stoff.ipynb` for cataloging the substances.
   
3. **Generate Shapefiles**:
   - Use `Generate_shape_files.ipynb` to generate shapefiles for visualization in QGIS.
   
4. **Visualize the Data**:
   - Open the `Geodata_Task_3.qgz` project in QGIS.
   - Use the Temporal Controller to animate the data across different time periods.
   
5. **Export the Movie**:
   - Export images from QGIS at regular intervals and compile them into a video using video editing tools.

---

### Data Sources:
All nitrate concentration data was sourced from **OpenHygrisC**, with datasets for different time periods:
- [OpenHygrisC Dataset Link](https://www.opengeodata.nrw.de/produkte/umwelt_klima/wasser/grundwasser/hygrisc/)

---

This README provides a detailed step-by-step guide for setting up and running the OpenHygrisC nitrate data project, culminating in a temporal visualization that displays how nitrate levels in groundwater have changed over time.
