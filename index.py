import pickle
import streamlit as st
import streamlit.components.v1 as components
from APIs import *

import pandas as pd

def rev(_id):
    s_url = 'https://api.themoviedb.org/3/movie/580489/reviews?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1'
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dictionaries = s_data['results']
    vkey = "content"
    lvalues = [item[vkey] for item in dictionaries]
    # df = pd.DataFrame(lvalues)
    return lvalues[_id]

st.image('images/hed.jpeg')

r_date = '<p style="font-family:Fantasy; color:red;font-size: 15px;">Release Date</p>'
r_over = '<p style="font-family:Fantasy; color:red;font-size: 15px;">Overview</p>'
r_btn = '<p style="font-family:Fantasy; color:red;font-size: 15px;">Review & Sentiments</p>'
r_vote = '<p style="font-family:Fantasy; color:red;font-size: 15px;"> Rating : </p>'

# st.markdown(header, unsafe_allow_html=True)

st.header("Popular Movies")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image(pop_mov_poster(0))
    with st.expander(pop_mov_name(0)):
        st.write(r_date, pop_rel_date(0), unsafe_allow_html=True)
        # st.write(r_over,pop_mov_overview(0), unsafe_allow_html=True)
        btn1 = st.button('know more..', key="1")

with col2:
    st.image(pop_mov_poster(1))
    with st.expander(pop_mov_name(1)):
        st.write(r_date, pop_rel_date(1), unsafe_allow_html=True)
        # st.write(r_over, pop_mov_overview(1), unsafe_allow_html=True)
        btn2 = st.button('know more..', key="2")

with col3:
    st.image(pop_mov_poster(2))
    with st.expander(pop_mov_name(2)):
        st.write(r_date, pop_rel_date(2), unsafe_allow_html=True)
        # st.write(r_over, pop_mov_overview(2), unsafe_allow_html=True)
        btn3 = st.button('know more..', key="3")

with col4:
    st.image(pop_mov_poster(3))
    with st.expander(pop_mov_name(3)):
        st.write(r_date, pop_rel_date(3), unsafe_allow_html=True)
        # st.write(r_over, pop_mov_overview(3), unsafe_allow_html=True)
        btn4 = st.button('know more..', key="4")

#Upcoming movies
st.header("Upcoming Movies")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image(up_mov_poster(0))
    with st.expander(pop_mov_name(0)):
        st.write(r_date, up_rel_date(0), unsafe_allow_html=True)
        # st.write(r_over,up_mov_overview(0), unsafe_allow_html=True)
        btn5 = st.button('know more..', key="5")

with col2:
    st.image(up_mov_poster(1))
    with st.expander(up_mov_name(1)):
        st.write(r_date, up_rel_date(1), unsafe_allow_html=True)
        btn6 = st.button('know more..', key="6")

with col3:
    st.image(up_mov_poster(2))
    with st.expander(up_mov_name(2)):
        st.write(r_date, up_rel_date(2), unsafe_allow_html=True)
        btn7 = st.button('know more..', key="7")

with col4:
    st.image(up_mov_poster(3))
    with st.expander(up_mov_name(3)):
        st.write(r_date, up_rel_date(3), unsafe_allow_html=True)
        btn8 = st.button('know more..', key="8")


#Tv shows
st.header("Top Rated ")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image(tv_mov_poster(0))
    with st.expander(tv_mov_name(0)):
        st.write(r_date, tv_rel_date(0), unsafe_allow_html=True)
        btn9 = st.button('know more..', key="9")


with col2:
    st.image(tv_mov_poster(1))
    with st.expander(tv_mov_name(1)):
        st.write(r_date, tv_rel_date(1), unsafe_allow_html=True)
        btn10 = st.button('know more..', key="10")
with col3:
    st.image(tv_mov_poster(2))
    with st.expander(tv_mov_name(2)):
        st.write(r_date, tv_rel_date(2), unsafe_allow_html=True)
        btn11 = st.button('know more..', key="11")
with col4:
    st.image(tv_mov_poster(3))
    with st.expander(tv_mov_name(3)):
        st.write(r_date, tv_rel_date(3), unsafe_allow_html=True)
        btn12 = st.button('know more..', key="12")

st.image('images/sonic.gif',width=700)

#Sidebar
st.sidebar.header('Search here...')
movie_list = movies['title'].values
selected_movie = st.sidebar.selectbox(
    "",
    movie_list
)

s_button = st.sidebar.button('Rec Me')

if s_button:
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col2:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col2:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

if btn1:
    st.sidebar.title(pop_mov_name(0))
    st.sidebar.header(pop_vote(0))
    st.sidebar.write(pop_mov_overview(0))
    # st.sidebar.write(rev(0))

if btn2:
    st.sidebar.title(pop_mov_name(1))
    st.sidebar.header(pop_vote(1))
    st.sidebar.write(pop_mov_overview(1))

if btn3:
    st.sidebar.title(pop_mov_name(2))
    st.sidebar.header(pop_vote(2))
    st.sidebar.write(pop_mov_overview(2))

if btn4:
    st.sidebar.title(pop_mov_name(3))
    st.sidebar.header(pop_vote(3))
    st.sidebar.write(pop_mov_overview(3))

#up
if btn5:
    st.sidebar.title(up_mov_name(0))
    st.sidebar.header(up_vote(0))
    st.sidebar.write(up_mov_overview(0))
    # st.sidebar.write(rev(0))

if btn6:
    st.sidebar.title(up_mov_name(1))
    st.sidebar.header(up_vote(1))
    st.sidebar.write(up_mov_overview(1))

if btn7:
    st.sidebar.title(up_mov_name(2))
    st.sidebar.header(up_vote(2))
    st.sidebar.write(up_mov_overview(2))

if btn8:
    st.sidebar.title(up_mov_name(3))
    st.sidebar.header(up_vote(3))
    st.sidebar.write(up_mov_overview(3))

#top
if btn9:
    st.sidebar.title(tv_mov_name(0))
    st.sidebar.header(tv_vote(0))
    st.sidebar.write(tv_mov_overview(0))
    # st.sidebar.write(rev(0))

if btn10:
    st.sidebar.title(tv_mov_name(1))
    st.sidebar.header(tv_vote(1))
    st.sidebar.write(tv_mov_overview(1))

if btn11:
    st.sidebar.title(tv_mov_name(2))
    st.sidebar.header(tv_vote(2))
    st.sidebar.write(tv_mov_overview(2))

if btn12:
    st.sidebar.title(tv_mov_name(3))
    st.sidebar.header(tv_vote(3))
    st.sidebar.write(tv_mov_overview(3))

