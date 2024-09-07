# Task 4: 3D Map Creation and Animation Using QGIS and Python

## Overview:

In this task, we created a **3D map** using building footprint data in **QGIS**, exported frames, and visualized them using **Python** to generate a 3D animation of the map. The final output includes both an **MP4 video** and a **GIF animation**.

---

## Step-by-Step Solution:

### 1. **Creating the 3D Map in QGIS**

#### Objective:
The primary objective was to import building footprint data into QGIS and convert it into a 3D map for better visualization.

#### Solution:
- **Step 1**: Loaded the **Building Footprints** shapefile data into QGIS.
    - The **Building Footprints** data consists of multiple files:
        - `Building Footprints.shp`: Main file containing geometric data of buildings.
        - `Building Footprints.dbf`: Attribute data, including building heights.
        - `Building Footprints.prj`: Coordinate system definition.
        - `Building Footprints.shx`: Index file linking geometry and attributes.
        - `Building Footprints.cpg`: Encoding information.
- **Step 2**: Enabled the **3D map view** in QGIS and used the height attributes to extrude 2D building footprints into 3D models.
    - The building height values were used to give each footprint its vertical dimension, creating the 3D map.
- **Step 3**: Adjusted lighting, shadows, and camera angle within QGIS to enhance the 3D visualization.

### 2. **Exporting Frames from QGIS**

#### Objective:
To create a smooth 3D animation, frames were exported from QGIS at various angles.

#### Solution:
- **Step 1**: Used the **QGIS Temporal Controller** and the `Geodata_Task_4.qgz` project to export a series of images capturing different views of the 3D map.
- **Step 2**: The frames were saved in a sequence to be later used in animation generation. These frames captured various perspectives to produce a continuous 3D viewing experience.

### 3. **Generating the Animation Using Python**

#### Objective:
Using the exported frames, we compiled the animation into both **MP4** and **GIF** formats using a Python script.

#### Solution:
- **Step 1**: The **Python script** `GENERATE 3D MAP ANIMATION.ipynb` processed the exported images.
- **Step 2**: The frames were compiled into a smooth animation using **Python libraries**:
    - The MP4 version was created for higher resolution and video playback.
    - A GIF version was created for easy embedding and sharing.
- **Step 3**: Adjustments to frame rate and image sequencing were made to ensure smooth transitions in the final animation.

### Explanation of the 3D Map:

The **3D map** was constructed by using the building footprint shapefiles and extruding them vertically based on the attribute data for building heights. The animation created from this 3D map shows various perspectives of the city's structures, offering a clearer understanding of the spatial arrangement and vertical dimensions of the buildings.

---

## Final 3D Map Animation (GIF)

Below is the final output of the 3D map animation, visualized as a **GIF**. This showcases the smooth transitions of different camera angles, providing a dynamic view of the city's buildings.

### 3D Map Animation:
![3D Map Animation](3D%20Map%20Animation.gif)

---

## How to Run the Project:

### Requirements:
- **QGIS** with 3D View enabled.
- **Python** with libraries installed for image and video processing.

### Steps:
1. **Set Up QGIS**:
   - Open the `Geodata_Task_4.qgz` project in QGIS.
   - Load the building footprint shapefiles (`Building Footprints.shp`, etc.).
   - Use the QGIS 3D map view and set up the extrusion parameters based on the height data in the shapefile.

2. **Export Frames**:
   - Export images of the 3D map at different angles to create a sequence of frames for animation.

3. **Generate the Animation**:
   - Use the `GENERATE 3D MAP ANIMATION.ipynb` script to process the exported frames.
   - This script will generate both an MP4 video and a GIF animation.

---

## Files Included:
- **Building Footprints Shapefiles**:
    - `Building Footprints.shp`
    - `Building Footprints.dbf`
    - `Building Footprints.prj`
    - `Building Footprints.shx`
    - `Building Footprints.cpg`
- **QGIS Project File**: `Geodata_Task_4.qgz`
- **Python Script**: `GENERATE 3D MAP ANIMATION.ipynb`
- **Output Files**:
    - `3D Map Animation.mp4`: The final video animation.
    - `3D Map Animation.gif`: The GIF version of the animation.

---

This README provides a step-by-step explanation of how the 3D map was created, frames were exported, and the animation was generated using Python.
