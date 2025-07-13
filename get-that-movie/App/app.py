import streamlit as st
#from recommender import get_recommendations
import json
from pandas import read_csv

#load the precompute file
with open("precompute/movie_sims_dict.json", 'r') as f:
    map = json.load(f)

#load the movie dataset
data = read_csv("data/movie.csv")

movie_list = sorted(data['title'].tolist())
movie = st.selectbox("Choose a movie : ", movie_list)

if movie:
    st.write("You might also like!!!")
    st.write(f"Five Movies Similar to '{movie}' are :\n")
    movie_id = data[data['title'] == movie].index[0]
    similar_id = map[str(movie_id)]
    recommendations = data.iloc[similar_id]['title'].tolist()

    for i in range(1,6):
        st.write('- ', recommendations[i])