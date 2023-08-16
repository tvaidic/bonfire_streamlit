#imports first:
from pathlib import Path
import streamlit as st
import sys
import os

filepath = os.path.join(Path(__file__).parents[1])
print(filepath)

sys.path.insert(0, filepath)

from to_mongo import ToMongo
c = ToMongo()

# now we query database

'''
returns info about a card from our data base to a user in a freindly format
query the db base on user input then dislplay info back to then
when a user wants to query or search info we dont have a loacal file to ref we will want to be 
'''

answer = st.text_input("Enter a card name", value = 'Sol Ring')
st.write(list(c.cards.find({'name': answer})))