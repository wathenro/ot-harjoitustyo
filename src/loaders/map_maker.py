import numpy as np

class MapMaker():
    """Creation of the map of cities between start and end stations and
    rendering the designed track.

    Args:
        None
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
            if index==start_station:
                created_map[(y_coord-5):(y_coord+5),(x_coord-5):(x_coord+5),0]=0
                created_map[(y_coord-5):(y_coord+5),(x_coord-5):(x_coord+5),1]=100
                created_map[(y_coord-5):(y_coord+5),(x_coord-5):(x_coord+5),2]=0
            if index==end_station:
                created_map[(y_coord-5):(y_coord+5),(x_coord-5):(x_coord+5),0]=255
                created_map[(y_coord-5):(y_coord+5),(x_coord-5):(x_coord+5),1]=0
                created_map[(y_coord-5):(y_coord+5),(x_coord-5):(x_coord+5),2]=0

        return created_map,communities

    def get_scaling(self,communities,start_station,end_station):
        """Finds the coordinates for the start station and endstation and from
        calculates and returns the scale of the map so that the distance between
        mentioned stations is as high as possible on the drawn map.

        Args:
            start_station: Start city for the railway line
            end_station: End city for the railway line
            communities: Pandas-dataframe with cities

        Returns:
            start_x: longitude for the westernmost of start station/end station
            start_y: latitude for the southernmost of start station/end station
            end_x: longitude for the easternnmost of start station/end station
            end_y: latitude for the easternrnmost of start station/end station
            x_scale: longitudial distance between start station/end station
            y_scale: latitudial distance between start station/end station
        """
        start_x=min(communities["Longitude"][start_station],communities["Longitude"][end_station])
        start_y=min(communities["Latitude"][start_station],communities["Latitude"][end_station])
        end_x=max(communities["Longitude"][start_station],communities["Longitude"][end_station])
        end_y=max(communities["Latitude"][start_station],communities["Latitude"][end_station])
        x_scale=abs(start_x-end_x)
        y_scale=abs(start_y-end_y)

        return start_x,start_y,end_x,end_y,x_scale,y_scale

    def draw_track(self,created_map,c_on_map,best_track,start_station,end_station):
        """Plots optimized track to numpy.array map for visulization

        Args:
            created_map: np.array where cities and tracks are marked
            c_on_map: pandas dataframe with coordinates for the cities
            best_track: optimized route as a string
            start_station: string, name of the start station
            end_station: string, name of the end station

        Returns:
            created_map: np.array with cities and optimized track rendered

        """
        track_cities=best_track.split("-")
        first_city=track_cities.pop(0)
        start_x,start_y,_,_,x_scale,y_scale=\
            self.get_scaling(c_on_map,start_station,end_station)
        for city in track_cities:
            second_city=city

            x_raw_first=(c_on_map["Longitude"][first_city]-start_x)/x_scale
            y_raw_first=(c_on_map["Latitude"][first_city]-start_y)/y_scale
            x_coord_first=int(x_raw_first*400)
            y_coord_first=int(y_raw_first*400)

            x_raw_second=(c_on_map["Longitude"][second_city]-start_x)/x_scale
            y_raw_second=(c_on_map["Latitude"][second_city]-start_y)/y_scale
            x_coord_second=int(x_raw_second*400)
            y_coord_second=int(y_raw_second*400)

            try:
                slope=(y_coord_second-y_coord_first)/(x_coord_second-x_coord_first)
            except ZeroDivisionError:
                slope=100

            for x_draw in range(0,abs(x_coord_first-x_coord_second)):
                x_point=100+min(x_coord_first,x_coord_second)+x_draw
                if x_coord_first<x_coord_second:
                    y_point=int(500-y_coord_first-slope*x_draw)
                else:
                    y_point=int(500-y_coord_second-slope*x_draw)
                created_map[y_point,(x_point-5):(x_point+1),0:3]=0

            first_city=second_city

        return created_map
                