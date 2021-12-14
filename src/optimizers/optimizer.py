import pandas as pd
import numpy as np
from random import choice

from haversine import haversine

class Optimizer():
    def __init__(self):
        pass
    def optimizer(self,start_station,end_station,created_map,c_on_map,max_track):
        distance_matrix=self.get_distance_matrix(c_on_map)
        stops=list(distance_matrix.index)
        stops.remove(start_station)
        print(distance_matrix)
        valid_tracks={}
        
        track=start_station+"-"
        for i in range(1,1000000):
            flag=0
            chosen_stops=[]
            track_length=0
            previous_station=start_station
            track=start_station+"-"
            population=int(c_on_map["Population"][start_station])
            
            while flag==0:
                stop_candidate=choice(stops)
                if stop_candidate not in chosen_stops:
                    chosen_stops.append(stop_candidate)
                    track_length+=distance_matrix[previous_station][stop_candidate]
                    track+=stop_candidate+"-"
                    population+=int(c_on_map["Population"][stop_candidate])
                    previous_station=stop_candidate
                   
                else:
                    continue
                if track_length>max_track:
                    flag=1
                else:
                    if stop_candidate==end_station:
                        if track[:-1] not in valid_tracks:
                            valid_tracks[track[:-1]]=(population,round(track_length,3))
                            flag=1
                        else:
                            flag=1
            
        best_track=""
        max_pop=1
        for track in valid_tracks:
            if valid_tracks[track][0]>max_pop:
                max_pop=valid_tracks[track][0]
                best_track=track

        if best_track!="":
            return created_map,c_on_map,valid_tracks[best_track][1],\
                valid_tracks[best_track][0],best_track
        
        else:
            return created_map,c_on_map,0,0,""
            
    
    def get_distance_matrix(self,c_on_map):
        distance_matrix=pd.DataFrame(np.zeros((c_on_map.shape[0],c_on_map.shape[0]))\
            ,index=c_on_map.index,columns=c_on_map.index)
        for city_name in distance_matrix.index:
            for other_city_name in distance_matrix.index:
                distance_matrix[city_name][other_city_name]=\
                    haversine((c_on_map["Latitude"][city_name],\
                    c_on_map["Longitude"][city_name]),\
                    (c_on_map["Latitude"][other_city_name],\
                    c_on_map["Longitude"][other_city_name]))
        return distance_matrix
