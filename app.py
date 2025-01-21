# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     requests.get('https://api.themoviedb.org/3/movie/65?api_key=7bbb8a89d3aeb34cb657deaa7923e56d&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
#
#
#
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movie_list = sorted(list(enumerate(similarity[0])), reverse=True, key=lambda x: x[1])[1:6]
#     recommended_movies=[]
#     recommended_movies_posters = []
#     for i in movie_list:
#         # fetch poster via API
#         movie_id=movies.iloc[i[0]].movie_id
#         # fetch poster via API
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters
#
# movies_dict = pickle.load(open('movies_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl','rb'))
#
#
# st.title('Movie Recommender System')
# selected_movie_name = st.selectbox(
# 'these are the movies', movies['title'].values
# )
#
# if st.button('Recommend'):
#     name, posters = recommend(selected_movie_name)
#
#     col1, col2, col3, col4, col5 = st.beta_columnns(5)
#
#     with col1:
#         st.header(name[0])
#         st.image(posters[0])
#     with col2:
#         st.header(name[1])
#         st.image(posters[1])
#     with col3:
#         st.header(name[2])
#         st.image(posters[2])
#     with col4:
#         st.header(name[3])
#         st.image([posters[3]])
#     with col5:
#         st.header(name[4])str
#         st.image(posters[4])
#
#     for i in recommendations:
#         st.write(i)

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=7bbb8a89d3aeb34cb657deaa7923e56d&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('MovieMatch: Your Personalized Recommender')

selected_movie_name = st.selectbox(
    'Find your Match', movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])