import requests
import pickle

movies = pickle.load(open('Data/movie_list.pkl','rb'))
similarity = pickle.load(open('Data/similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:7]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

def pop_mov_ids(id):
    url = "https://api.themoviedb.org/3/movie/popular?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1"
    data = requests.get(url)
    data = data.json()
    dict = data['results']
    lst = list(dict)
    date = 'id'
    ids = [ item[date] for item in dict]
    return ids[id]

# def pop_vote(id):
#     url = "https://api.themoviedb.org/3/movie/566525/reviews?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1"
#     data = requests.get(url)
#     data = data.json()
#     dict = data['results']
#     lst = list(dict)
#     date = 'content'
#     auth = 'author'
#     author = [item[auth] for item in dict]
#     dates = [ item[date] for item in dict]
#     df = pd.DataFrame(dates, author)
#     return dates[id]



def pop_mov_overview(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dictionaries = s_data['results']
    listofdic = list(dictionaries)
    vkey = "overview"
    lvalues = [item[vkey] for item in dictionaries]
    return lvalues[movie_id]

def pop_mov_name(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dit = s_data['results']
    lst = list(dit)
    n = 'title'
    lvalues = [item[n] for item in dit]
    return lvalues[movie_id]

#popular movies Posters
def pop_mov_poster(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    pop_mov = s_data['results']
    mov = list(pop_mov)
    pop_path = 'poster_path'
    full_path = "https://image.tmdb.org/t/p/w500/"
    lvalues = [item[pop_path] for item in pop_mov]
    final_poster = full_path + lvalues[movie_id]
    return final_poster

#popular movies dates
def pop_rel_date(movie_id):
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1'
    data = requests.get(url)
    data = data.json()
    dict = data['results']
    lst = list(dict)
    date = 'release_date'
    lvalues = [item[date] for item in dict]
    return lvalues[movie_id]

def pop_vote(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/popular?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dit = s_data['results']
    lst = list(dit)
    n = 'vote_average'
    lvalues = [item[n] for item in dit]
    r = "Rating : "
    full_values = r + str(lvalues[movie_id])
    return full_values


#rewbding Movies
def up_vote(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/upcoming?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dit = s_data['results']
    lst = list(dit)
    n = 'vote_average'
    lvalues = [item[n] for item in dit]
    r = "Rating : "
    full_values = r + str(lvalues[movie_id])
    return full_values

def up_mov_overview(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/upcoming?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dictionaries = s_data['results']
    listofdic = list(dictionaries)
    vkey = "overview"
    lvalues = [item[vkey] for item in dictionaries]
    o = "Overview : "
    full = o + lvalues[movie_id]
    return full

def up_mov_name(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/upcoming?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dit = s_data['results']
    lst = list(dit)
    n = 'title'
    lvalues = [item[n] for item in dit]
    return lvalues[movie_id]

def up_mov_poster(movie_id):
    s_url = "https://api.themoviedb.org/3/movie/upcoming?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    pop_mov = s_data['results']
    mov = list(pop_mov)
    pop_path = 'poster_path'
    full_path = "https://image.tmdb.org/t/p/w500/"
    lvalues = [item[pop_path] for item in pop_mov]
    final_poster = full_path + lvalues[movie_id]
    return final_poster

def up_rel_date(movie_id):
    url = 'https://api.themoviedb.org/3/movie/upcoming?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1'
    data = requests.get(url)
    data = data.json()
    dict = data['results']
    lst = list(dict)
    date = 'release_date'
    lvalues = [item[date] for item in dict]
    return lvalues[movie_id]

#trending Movies
def tr_vote(movie_id):
    s_url = "https://api.themoviedb.org/3/trending/all/day?api_key=7d4a41327f888028ccc0736e8b8ac429"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dit = s_data['results']
    lst = list(dit)
    n = 'vote_average'
    lvalues = [item[n] for item in dit]
    r = "Rating : "
    full_values = r + str(lvalues[movie_id])
    return full_values

def tr_mov_overview(movie_id):
    s_url = "https://api.themoviedb.org/3/trending/all/day?api_key=7d4a41327f888028ccc0736e8b8ac429"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dictionaries = s_data['results']
    listofdic = list(dictionaries)
    vkey = "overview"
    lvalues = [item[vkey] for item in dictionaries]
    o = "Overview : "
    full = o + lvalues[movie_id]
    return full

def tr_mov_name(movie_id):
    s_url = "https://api.themoviedb.org/3/trending/all/day?api_key=7d4a41327f888028ccc0736e8b8ac429"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dit = s_data['results']
    lst = list(dit)
    n = 'name'
    lvalues = [item[n] for item in dit]
    return lvalues[movie_id]

def tr_mov_poster(movie_id):
    s_url = "https://api.themoviedb.org/3/trending/all/day?api_key=7d4a41327f888028ccc0736e8b8ac429"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    pop_mov = s_data['results']
    mov = list(pop_mov)
    pop_path = 'poster_path'
    full_path = "https://image.tmdb.org/t/p/w500/"
    lvalues = [item[pop_path] for item in pop_mov]
    final_poster = full_path + lvalues[movie_id]
    return final_poster

def tr_rel_date(movie_id):
    url = 'https://api.themoviedb.org/3/trending/all/day?api_key=7d4a41327f888028ccc0736e8b8ac429'
    data = requests.get(url)
    data = data.json()
    dict = data['results']
    lst = list(dict)
    date = 'release_date'
    lvalues = [item[date] for item in dict]
    return lvalues[movie_id]
#TV Shows
def tv_vote(movie_id):
    s_url = "https://api.themoviedb.org/3/tv/top_rated?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dit = s_data['results']
    lst = list(dit)
    n = 'vote_average'
    lvalues = [item[n] for item in dit]
    r = "Rating : "
    full_values = r + str(lvalues[movie_id])
    return full_values


def tv_mov_overview(movie_id):
    s_url = "https://api.themoviedb.org/3/tv/top_rated?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dictionaries = s_data['results']
    listofdic = list(dictionaries)
    vkey = "overview"
    lvalues = [item[vkey] for item in dictionaries]
    return lvalues[movie_id]

def tv_mov_name(movie_id):
    s_url = "https://api.themoviedb.org/3/tv/top_rated?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    dit = s_data['results']
    lst = list(dit)
    n = 'name'
    lvalues = [item[n] for item in dit]
    return lvalues[movie_id]

def tv_mov_poster(movie_id):
    s_url = "https://api.themoviedb.org/3/tv/top_rated?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1"
    s_data = requests.get(s_url)
    s_data = s_data.json()
    pop_mov = s_data['results']
    mov = list(pop_mov)
    pop_path = 'poster_path'
    full_path = "https://image.tmdb.org/t/p/w500/"
    lvalues = [item[pop_path] for item in pop_mov]
    final_poster = full_path + lvalues[movie_id]
    return final_poster

def tv_rel_date(movie_id):
    url = 'https://api.themoviedb.org/3/tv/top_rated?api_key=7d4a41327f888028ccc0736e8b8ac429&language=en-US&page=1'
    data = requests.get(url)
    data = data.json()
    dict = data['results']
    lst = list(dict)
    date = 'first_air_date'
    lvalues = [item[date] for item in dict]
    return lvalues[movie_id]