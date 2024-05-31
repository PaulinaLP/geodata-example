import geopandas as gpd
import pandas as pd
import os
import sys

from Code import coast_line
from Code.map_point import MapPoint
from Code import ine_geo
from Code import ine_data

# global variables
SCRIPT_PATH = os.path.abspath(os.path.dirname(sys.argv[0]))
OUTPUT_PATH = os.path.join(SCRIPT_PATH, 'output')
INPUT_PATH = os.path.join(SCRIPT_PATH, 'input')


if __name__ == '__main__':
    # loading coast data
    coast_ln = gpd.read_file(os.path.join(INPUT_PATH, 'lineaCosta\\COSTA.shp'))
    coast_gdf = coast_line.create_coast_line(coast_ln, printing=0)
    # loading ine data for matching geo points with corresponding section
    ine_sections = gpd.read_file(os.path.join(INPUT_PATH, 'ine\\SECC_CE_20240101.shp'))
    # loading ine data for sections (income & demography)
    ine_income_data = pd.read_csv(os.path.join(INPUT_PATH, 'ine_data\\30824.csv'), sep=';')
    ine_demography_data = pd.read_csv(os.path.join(INPUT_PATH, 'ine_data\\30832.csv'), sep=';')
    # preprocessing the tables
    pivot_income = ine_data.get_last_data(ine_income_data, ine_type='income')
    pivot_demography = ine_data.get_last_data(ine_demography_data, ine_type='demo')
    # deleting original tables to get more memory
    del ine_demography_data
    del ine_income_data
    # selecting 2 points (as example)
    madrid = MapPoint(-3.7038, 40.4168, name='Madrid - centre')
    barcelona = MapPoint(2.1734, 41.3851, name='Barcelona - centre')
    for spanish_point in [madrid, barcelona]:
        # showing the distance between the point and the coast
        distance = spanish_point.calculate_distance(coast_gdf,'coast', printing=1)
        # showing the section number for the point
        cusec = ine_geo.ine_get_cusec(spanish_point, ine_sections, printing=1)
        # showing income and demo data for the point
        ine_data.get_section_data(pivot_income, cusec, printing=1)
        ine_data.get_section_data(pivot_demography, cusec, printing=1)





