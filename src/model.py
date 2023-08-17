from pathlib import Path
from PIL import Image
from io import BytesIO
import pandas as pd
import requests
import pickle
import ast
import os
import re

# step 1 establiish data directory
folder_dir = os.path.join(Path(__file__).parents[0], 'data')
print(folder_dir)

# Second step : for vectorization
#create a dummy function that takes in a doc and returns a doc
def dummy_func(doc):
    return doc

class Model:
    def __init__(self):
        self.df = pd.read_csv(f'{folder_dir}/oracale_cards.csv', low_memory=False)
        self.nnm = pickle.load(open(f'{folder_dir}/model', 'rb'))
        self.stop_words = ['on', 'the', 'of', 'and']
        self.cap_stop_words = [w.title() for w in self.stop_words]
    
    def card_names_fix(self, card_name: str):
        self.string = re.sub(
            r"[A-Za-z]+('[A-Za-z]+)?",
            lambda x: x.group(0)[0].upper() +
            x.group(0)[1:].lower() if x.group(0) not in self.stop_words or self.cap_stop_words and card_name.startswith(x.group(0)) else x.group(0).lower(),
            card_name
        )

        # split the string:
        self.split_str= self.string.split()
        print(self.split_str)
        c = 0 
        for name in self.split_str:
            if '-' in name:
                name = name.title()
                c+=1
            elif name[1] == "'":
                name = name[0:3].upper()+ name[3:]
                self.split_str[c] = name
                c+=1
            else:
                c+=1
        return ' '.join(self.split_str)
    
    def nn(self, card_name: str):
        '''
        input: card_name -> str type object recieved from user input
        output: 9 recomended cards based fo the cosine smilarity between each mapped out card by model
        '''
        self.card_name = self.card_names_fix(card_name)
        self.vect = pickle.load(open(f'{folder_dir}/vect', 'rb'))
        self.names = []
        self.doc = self.vect.transform(
            self.df['lemmas'][self.df['name'] == self.card_name]
        )
        self.n_index = self.nnm.kneighbors(
            self.doc, return_distance=False
        )
        for index in self.n_index[0]:
            if index!= self.df[self.df['name']==self.card_name].index:
                self.names.append(self.df['name'][index])
        return self.names
    
    def img_return(self, card_name: str):
        s = self.df[self.df['name'] == self.card_names_fix(card_name)]['image_uris']
        for k in s:
            img_dic = ast.literal_eval(k)
        img_str = img_dic['normal']
        response = requests.get(img_str)
        img = Image.open(BytesIO(response.content))
        return img
    
    def recomended_cards(self, card_name: str):
        names = self.nn(card_name)
        return [self.img_return(name) for name in names]


if __name__ == '__main__':
    c = Model()
    print(c.card_names_fix("d'vorrah"))