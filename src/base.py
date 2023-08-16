import requests
import pandas as pd

class Base:
    '''
    Class handles all requests to the Scryfall API and returns the data from its initialization.

    Class will have the following methods:
    return_url(): return the api url that we are currently working with
    get_data(): get the data from the api and create a pandas dataframe from it

    '''
    def __init__(self):
        self.api_url = 'https://api.scryfall.com/bulk-data'
        self.get_data()

    def return_url(self):
        return self.api_url
    
    def get_data(self):
        '''
        Scraping data from api and creating a pandas dataframe from it.
        '''
        response = requests.get(self.api_url)
        response1 = requests.get(response.json()['data'][0]['download_uri'])
        self.df = pd.DataFrame.from_dict(response1.json())
        return self.df


if __name__ == '__main__':
    c = Base()
    c.df.to_csv(r'src/data/oracale_cards.csv', index=False)