import shapely
import geopandas as gpd


class MapPoint:
    def __init__(self,  longitude: float, latitude: float, name='no_name', crs: object = "EPSG:4326"):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.crs = crs
        self.gpd_image = gpd.GeoSeries([shapely.Point(longitude, latitude)], crs=crs)

    def change_crs(self, new_crs: int):
        self._check_type(new_crs, int)
        self.gpd_image = self.gpd_image.to_crs(epsg=new_crs)
        return self

    def calculate_distance(self, polygon: gpd.GeoDataFrame, polygon_name='polygon', printing=0):
        self._check_type(polygon, gpd.GeoDataFrame)
        # Reproject to EPSG:3857 (Pseudo-Mercator)
        polygon = polygon.to_crs(epsg=3857)
        self.change_crs(3857)
        distance_meters = polygon.distance(self.gpd_image[0])[0]
        distance_km = distance_meters / 1000
        if printing == 1:
            print(f'Distance from {self.name} to {polygon_name} is {distance_km} km')
        return distance_km

    def _check_type(self, value, expected_type):
        if not isinstance(value, expected_type):
            raise TypeError(f"Expected value to be of type {expected_type.__name__}, got {type(value).__name__}")