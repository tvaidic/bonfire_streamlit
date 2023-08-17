import streamlit as st
from pathlib import Path
import sys
import os

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from model import dummy_func, Model
m = Model()

st.title('Recomended Cards:')

card_name = st.text_input('Enter card name for what recomdations you would like:')

if st.button('submit card'):
    st.image(m.img_return(card_name))
    img_list = m.recomended_cards(card_name)
    st.write(
        f'Here are the {len(img_list)} cards that are recommended cards for {card_name.title()}'
    )
    col1, col2, col3 = st.columns(3)
    col1.image(img_list[0:3])
    col2.image(img_list[3:6])
    col3.image(img_list[6:9])
  