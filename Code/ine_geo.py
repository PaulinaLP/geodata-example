import geopandas as gpd
from Code.map_point import MapPoint


# function to get the ID for section for a geo point
def ine_get_cusec(map_point: MapPoint, ine_sections: gpd.GeoDataFrame, printing=0):
    map_point.change_crs(25830)
    ine_sections['point'] = ine_sections['geometry'].apply(lambda x: x.contains(map_point.gpd_image))
    point = ine_sections[ine_sections['point']]
    first_cusec_value = point.iloc[0]['CUSEC']
    if printing == 1:
        print(f'The section for {map_point.name} is {first_cusec_value}')
    return first_cusec_value