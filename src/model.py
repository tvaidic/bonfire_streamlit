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
def dummy_function(doc):
    return doc

class Model:
    def __init__(self):
        self.df = pd.read_csv(f'{folder_dir}/oracale_cards.csv', low_memory=False)
        