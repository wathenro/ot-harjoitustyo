import pandas as pd
import requests

class LocLoader():
    """Data loader class

    Args:
        None
    """

    def __init__(self):
        self.load_successful=False

    def location_loader(self):
        """Downloads Finlands communities from Wikipedia or alternatively file.

        Attributes:
            None

        Returns:
            communities: pandas dataframe with communities as index, longitude,
            latitude and population as columns
        """

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

        except requests.exceptions.RequestException:
            try:
                communities=pd.read_csv("src/data/communities.csv",index_col=0,header=0)
            except FileNotFoundError:
                communities=pd.read_csv("data/communities.csv",index_col=0,header=0)
            print("Did not get from the web, loaded local.")
        communities=self.population_loader(communities)
        return communities

    def population_loader(self,communities):
        """Gets population data from file.

        Attributes:
            communities: pandas dataframe with Finnish communities

        Returns:
            communities: pandas dataframe injected as attribute with
            added population data
        """
        try:
            population_data=pd.read_csv("src/data/population.csv",encoding="utf-8")
        except FileNotFoundError:
            population_data=pd.read_csv("data/population.csv",encoding="utf-8")
        population_data.set_index(population_data["Kunta"],inplace=True)
        population_data.drop(columns="Kunta",inplace=True)
        communities = pd.merge(population_data, communities, left_index=True, right_index=True)

        return communities
        