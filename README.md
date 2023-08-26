# UR5e Component Assembly with Python
This section involves the assembly process utilizing Python scripts along with tools like location dictionaries, OCR for identifying component positions, and ArUco for pose estimation.

# Camera Calibration
This directory is designated for obtaining camera parameters.

# Assembly using Python Codes for UR5e
Contained within this folder are operations related to material handling with the Universal Robot 5e. These tasks are carried out by leveraging its communication protocol.
    RTDE_moveL.py: Assembly involving RTDE communication.
    Socket_moveL.ipynb: Assembly involving Socket communication.

# Component Assembly with Dictionary
This directory focuses on material handling using predefined component locations stored in dictionaries.
    point_data.py: Creation of a dictionary encompassing source and destination locations for components.
    Component_handling_with_Dictionary.py: Primary Python file orchestrating the looping process through component locations.

# Component Identification with OCR
In this section, material handling is addressed when components are repositioned within the jig location.
    destinationl.py: Defines destination locations of components processed in capture position 1.
    destinationr.py: Defines destination locations of components processed in capture position 2.
    points1.py & points2.py: These files contain respective component locations obtained through OCR library usage.
    trial(Cap1) & trial(Cap2): Programs where image processing and RTDE protocols are iteratively implemented.

# Random Component Identification within Workspace
Utilizing ArUco markers, this category identifies component orientations, subsequently transmitted to the TCP to facilitate PICK and PLACE tasks.

# Transformation Matrix (via 4-Point Projection Method)
This folder pertains to acquiring the transformation matrix necessary for converting pixel coordinates from frames into real-world robot coordinates.
    4_Points_Projection.ipynb: Program for obtaining pixel coordinates from image/frame inputs.
    3D_frame_transformation.ipynb: Program to compute the transformation matrix. This involves inputting four points from image/frame pixel coordinates and their corresponding robot coordinates.
