import streamlit as st
#from recommender import get_recommendations
import json
from pandas import read_csv

#load the precompute file
with open("get-that-movie/precompute/movie_sims_dict.json", 'r') as f:
    map = json.load(f)

#load the movie dataset
data = read_csv("get-that-movie/data/movie.csv")

movie_list = sorted(data['title'].tolist())
movie = st.selectbox("Choose a movie : ", movie_list)

if movie:
    st.write("You might also like!!!")
    st.write(f"Five Movies Similar to '{movie}' are :\n")
    movie_id = data[data['title'] == movie].index[0]
    similar_id = map[str(movie_id)]
    recommendations = data.iloc[similar_id]['title'].tolist()

    disp = 0
    count = 0
    while count != 5:
        if recommendations[disp] != movie:
            st.write("-", recommendations[disp])
            count += 1
            disp += 1
        else:
            disp += 1