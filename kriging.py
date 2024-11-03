# -*- coding: utf-8 -*-
"""kriging.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/mariammemon21/15308ff63650011e98b84218fbd1f4d8/kriging.ipynb
"""

pip install numpy pandas matplotlib scipy pykrige

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging

# Load the dataset (replace with the correct path if needed)
file_path = 'K2.xlsx'
data = pd.read_excel(file_path)

# Extracting relevant columns from the dataset
latitude = data['Latitude'].values
longitude = data['Longitude'].values
pH_values = data['pH '].values

# Setting up the grid for interpolation
grid_lat = np.linspace(min(latitude), max(latitude), 100)
grid_lon = np.linspace(min(longitude), max(longitude), 100)

# Performing Ordinary Kriging
OK = OrdinaryKriging(
    longitude, latitude, moisture_values,
    variogram_model='linear',
    verbose=False, enable_plotting=False
)

# Generating kriged estimates for the grid
z, ss = OK.execute('grid', grid_lon, grid_lat)

# Plotting the results with a color map suitable for pH representation
plt.figure(figsize=(10, 8))
plt.contourf(grid_lon, grid_lat, z, cmap='coolwarm')  # Use coolwarm colormap
plt.scatter(longitude, latitude, c=moisture_values, edgecolor='black', s=30)
plt.title('Spatial Mapping of pH using Kriging')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='pH')
plt.show()