import pandas as pd
import requests


class LocLoader():

    def __init__(self):
        self.load_successful=False

    def location_loader(self):

        try:
            finnish_communities=\
                "https://fi.wikipedia.org/wiki/"+\
                "Luettelo_Suomen_kuntien_koordinaateista#Nykyiset_kunnat"
            communities=pd.read_html(requests.get(finnish_communities).content)[2]
            communities[["Latitude","Longitude"]]=\
                communities["Koordinaatit"].str.split("°N, ",expand=True)
            del communities["Koordinaatit"]
            communities["Longitude"]=communities["Longitude"].str.replace("°E","")
            communities.set_index(communities["Kunta"],inplace=True)
            del communities["Kunta"]
            communities[["Latitude","Longitude"]]\
                =communities[["Latitude","Longitude"]].apply(pd.to_numeric, errors='coerce', axis=1)
            #communities.to_csv("./src/data/communities.csv")

        except:
            communities=pd.read_csv("./src/data/communities.csv",index_col=0,header=0)

        return communities
