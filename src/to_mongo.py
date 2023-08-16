#Import statements
from base import Base
from dotenv import load_dotenv
import pymongo
import os

# Class Declaration:
class ToMongo(Base):
    '''
    designed as a class to transport the data from base to a mongo db instance
    initializes an instance of the inherited class

    defined methods are as follows:
    upload_one_by_one(): uploads pieces of infor to a database one by one over an iterable structure
    upload_collection(): uploads entire doc of items to mongo db
    delete_collection(): deletes entire doc of items from mongo db
    '''
    def __init__(self):
        Base.__init__(self)
        load_dotenv()
        self.user = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')
        self.mongo_url = os.getenv('MONGO_URL')
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client.db
        self.cards = self.db.cards 
        self.df.set_index('id', inplace=True)
    
    def upload_collection(self):
        '''
        Uploads entire collection of items to mongo db
        beware! there is a maximum upload size of 1000 items
        limtations to the ammount of data that you can upload at a time
        '''
        self.cards.insert_many([self.df.to_dict()])
    
    def upload_one_by_one(self):
        '''
        uploads our items one by one
        '''
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())
if __name__ == '__main__':
    c = ToMongo()
    print('successfully connected to mongo db')
    c.upload_one_by_one()
    print('great success')