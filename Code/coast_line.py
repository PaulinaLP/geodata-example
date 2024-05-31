import geopandas as gpd
import matplotlib.pyplot as plt


def create_coast_line(coast_line, printing=0):
    coast_line_closed=coast_line[(coast_line['CIERRACOST'] == 't') & (coast_line['BAJAMAR'] == 't') & (coast_line['FEATURE'].isin(['COALNE','SLCONS']))]
    coast_polygon = coast_line_closed.unary_union
    coast_polygon_gdf= gpd.GeoDataFrame(geometry=[coast_polygon])
    if coast_polygon_gdf.crs is None:
        coast_polygon_gdf.set_crs(epsg=4326, inplace=True)
    if printing == 1:
        coast_polygon_gdf.plot()
        plt.title('Spanish coast')
        plt.show()
    return coast_polygon_gdf
