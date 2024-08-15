import streamlit as st
import requests

import pickle
st.header("Movies Recommendation")
class BlockUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "pandas._libs.internals" and name == "BlockManager":
            from pandas.core.internals.blocks import BlockManager
            return BlockManager
        return super().find_class(module, name)

with open('Artifacts/movie_list.pkl', 'rb') as f:
    movies = BlockUnpickler(f).load()



simulation = pickle.load(open('Artifacts/similarity.pkl','rb'))

movie_list = movies['title'].values
st.selectbox('You want to watch more movies like?',movie_list)