# GeoData_2024_3_Final_Group_K

**EE_3.07 Geodata Management Systems 2024-3 - Final Assignment**

---

## Overview

This repository contains the final assignment for the **Geodata Management Systems 2024-3** course. The assignment consists of multiple tasks that explore various geospatial data processing techniques using **QGIS**, **Python**, and **PostGIS**. Each task is documented with detailed steps and the necessary files for reproduction of the results.

### Structure of the Repository

- **TASK 1**: Warming Stripes NRW — Visualizing climate data for Baden-Württemberg using Python and Geopandas.
- **TASK 2**: Burial Mounds in Uedemer Hochwald — Georeferencing and analyzing burial mounds using QGIS.
- **TASK 3**: OpenHygrisC Nitrate Data — Spatio-temporal data animation using PostGIS and QGIS.
- **TASK 4**: 3D Map Creation and Animation — Creating a 3D map of building footprints and visualizing it as a video animation.

Each task folder contains:
1. The necessary **data files** (shapefiles, project files, etc.).
2. The **Jupyter notebooks** and **QGIS project files** used for analysis and visualization.
3. **README.md** files in each task folder that explain the step-by-step solutions for the tasks.

---

## Presentation Slides and Video

In addition to the tasks, a **PowerPoint presentation** has been created to summarize the results of our project. The presentation covers each task with an explanation of methods and results. The video presentation further explains the project outcomes.

### Video Presentation

In our video, I present the following:
1. **Task Overview**: Brief explanation of each task.
2. **Methods**: The approach used to tackle each task, without diving into code-level details.
3. **Results**: Demonstration of the results, including maps, animations, and key observations.

#### Video Requirements:

- The video presents the **slides** with the results for each task.
- I focused on methods and results, without explaining every detail of the code execution.
- I referred to the code files and QGIS projects for each task, enabling reproduction of the work.

---

### Link to the Video Presentation

You can watch my video presentation on the following link:

**[Project Video Presentation]([https://docs.google.com/presentation/d/1C_wXOnQQlhiCtxF2rJVxQ3R26xuAwhHK/edit?usp=drivesdk&ouid=114530524064471632044&rtpof=true&sd=true])**

---

## How to Reproduce the Work

### 1. Task 1: Warming Stripes Visualization
- **Objective**: Create a visualization of warming stripes for selected stations in Baden-Württemberg.
- **Method**: We used Python, Geopandas, and Seaborn to produce the warming stripes for multiple stations.
- **Files**: All files related to Task 1, including the Jupyter notebook and the processed data, can be found in the `TASK 1` folder.
- **Reproduction**: To reproduce the warming stripes, follow the steps in the `README.md` file in the `TASK 1` folder.

### 2. Task 2: Burial Mounds in Uedemer Hochwald
- **Objective**: Georeference a map of burial mounds and perform spatial analysis.
- **Method**: QGIS was used for georeferencing, hillshade model generation, and burial mound elevation analysis.
- **Files**: The QGIS project file and other related data can be found in the `TASK 2` folder.
- **Reproduction**: Follow the instructions in the `README.md` file in the `TASK 2` folder for a detailed guide on reproducing the georeferencing and spatial analysis.

### 3. Task 3: OpenHygrisC Nitrate Data
- **Objective**: Create a spatio-temporal animation of nitrate concentration using PostGIS and QGIS.
- **Method**: PostGIS was used to store and manage the nitrate concentration data, and QGIS’s temporal controller was used to animate the data over time.
- **Files**: SQL queries, Jupyter notebooks, and QGIS project files can be found in the `TASK 3` folder.
- **Reproduction**: The `README.md` file in the `TASK 3` folder provides step-by-step instructions for setting up the database and creating the animation.

### 4. Task 4: 3D Map Creation and Animation
- **Objective**: Create a 3D map of building footprints and visualize the map as an animated video.
- **Method**: The 3D map was created in QGIS using building footprint data, and Python was used to generate an MP4 video and GIF animation from exported frames.
- **Files**: Shapefiles, Python scripts, and QGIS project files can be found in the `TASK 4` folder.
- **Reproduction**: Detailed steps for creating the 3D map and animation are provided in the `README.md` file in the `TASK 4` folder.

---

## Running the Code

Each task has a separate set of instructions and requirements listed in the respective `README.md` file within the task folders. Make sure to follow the instructions carefully to reproduce the results.

### General Requirements
- **QGIS** with support for 3D map views.
- **Python** with the necessary libraries.
- **PostGIS** for database management in Task 3.

### Reproduction Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-link/GeoData_2024_3_Final_Group_K.git
   cd GeoData_2024_3_Final_Group_K
