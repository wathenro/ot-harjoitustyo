import numpy as np

class MapMaker():
    """Class for creation of the map of cities between start and end stations
    """
    def __init__(self):
        """Constructor

        """
        self.start_station=""
        self.end_station=""

    def make_map(self,start_station,end_station,communities):
        """Finds the cities between endstations and puts them on a map
           that is a numpy-grid.

        Args:
            start_station: Start city for the railway line
            end_station: End city for the railway line
            communities: Pandas-dataframe with all cities

        Returns:
            created_map: numpy-array with cities in correct locations
            communities: communities on map

        """
        start_x,start_y,end_x,end_y,x_scale,y_scale=\
            self.get_scaling(communities,start_station,end_station)
        created_map = np.zeros((512,512,3), dtype=np.uint8)+255

        for index, row in communities.iterrows():
            if not start_x<= row["Longitude"]<=end_x:
                communities.drop([index],axis=0,inplace=True)
                continue
            if not start_y<= row["Latitude"]<=end_y:
                communities.drop([index],axis=0,inplace=True)
                continue
            x_raw=(row["Longitude"]-start_x)/x_scale
            y_raw=(row["Latitude"]-start_y)/y_scale
            x_coord=int(100+x_raw*400)
            y_coord=int(500-y_raw*400)

            created_map[(y_coord-5):(y_coord+5),(x_coord-5):(x_coord+5),0:2]=100
            if index=="Helsinki":
                created_map[(y_coord-5):(y_coord+5),(x_coord-5):(x_coord+5),0:2]=0

        return created_map,communities

    def get_scaling(self,communities,start_station,end_station):
        start_x=min(communities["Longitude"][start_station],communities["Longitude"][end_station])
        start_y=min(communities["Latitude"][start_station],communities["Latitude"][end_station])
        end_x=max(communities["Longitude"][start_station],communities["Longitude"][end_station])
        end_y=max(communities["Latitude"][start_station],communities["Latitude"][end_station])
        x_scale=abs(start_x-end_x)
        y_scale=abs(start_y-end_y)

        return start_x,start_y,end_x,end_y,x_scale,y_scale
        