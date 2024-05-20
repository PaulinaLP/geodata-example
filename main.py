import geopandas as gpd
import shapely
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

from Code import coast_line
from Code.map_point import MapPoint

script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
output_path = os.path.join(script_path, 'output')
input_path = os.path.join(script_path, 'input')

coast_ln=gpd.read_file(os.path.join(input_path, 'lineaCosta\\COSTA.shp'))
coast_polygon_gdf = coast_line.create_coast_line(coast_ln, printing=0)

if __name__ == '__main__':
    # creating the polygon of coast line
    coast_ln = gpd.read_file(os.path.join(input_path, 'lineaCosta\\COSTA.shp'))
    coast_gdf = coast_line.create_coast_line(coast_ln, printing=0)
    # Reproject to EPSG:3857 (Pseudo-Mercator)
    coast_gdf_3857 = coast_gdf.to_crs(epsg=3857)
    # Define the random points for Madrid and Barcelona
    madrid = MapPoint(-3.7038, 40.4168, name='Madrid')
    barcelona = MapPoint(2.1734, 41.3851, name='Barcelona')
    madrid.change_crs(3857)
    barcelona.change_crs(3857)
    madrid.calculate_distance(coast_gdf_3857,'coast',printing=1)
    barcelona.calculate_distance(coast_gdf_3857, 'coast', printing=1)

#ine_sections=gpd.read_file(os.path.join(input_path, 'ine\\SECC_CE_20240101.shp'))
