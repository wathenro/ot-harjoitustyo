import pandas as pd
import requests

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
 