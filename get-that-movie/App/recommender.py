#imports
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(movie_watched, n = 5):
    #load the dataset
    data = pd.read_csv('data/movie.csv')

    #initialise the encoder
    encoder = MultiLabelBinarizer()

    #split genres from the full string
    data['genres'] = data['genres'].str.split('|')

    #This is pretty much similar to One Hot Encoder
    encoded_genre = encoder.fit_transform(data['genres'])

    #Dataframe of all genres
    df_genre = pd.DataFrame(encoded_genre, columns = encoder.classes_, index = data.index)

    #concat with main data
    data = pd.concat([data, df_genre], axis =1)
    data = data.drop(['genres'], axis = 1)

    #using corrwith isnt viable here so, I am using cosine similarity from sklearn
    #first, get the genres values
    genre_vals = df_genre.values

    #then I can make the similarity matrix
    similarity_matrix = cosine_similarity(genre_vals)

    #we get the indexes of that movie
    movie_index = data[data['title'] == movie_watched].index[0]
    
    #fetch similarity scores of that movie with others
    similarity_score = list(enumerate(similarity_matrix[movie_index]))

    #We do sorting of the movies in descending order of their similaity scores
    sorted_movies = sorted(similarity_score, key = lambda x: x[1], reverse = True)

    #Now we can get top 5 movies based on the most similarity scores
    #Of course we will exclude our input movie itself
    most_similar_movies = [data.iloc[i[0]]['title'] for i in sorted_movies[1:n+1]]

    return most_similar_movies