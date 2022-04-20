import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials




year="2002-01-02"
CLIENT_ID = "7bb6d4a7102547308df2916f3293b97c"
CLIENT_SECRET = "30931e6d3ed444fa880ca16452beb057"
URL_REDIRECT = "http://example.com"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                          client_secret=CLIENT_SECRET, redirect_uri=URL_REDIRECT,
                          scope="playlist-modify-private",
                          show_dialog=True,
                          cache_path="token.txt"
                          ))
# sp.get_access_token()
print(sp)


request = requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}")
request.raise_for_status()
data = request.text
# print(data)

soup = BeautifulSoup(data, "html.parser")
ak = soup.select(selector="li h3#title-of-a-story")

arsenal = [i.getText().strip().strip("\n") for i in ak]

year_here=year.split('-')[0]
song_uris=[]

user_id = sp.current_user()['id']
for i in arsenal:

    result=sp.search(q=f"track:{i} year:{year_here}", type="track")
    print(result)
    try:
        uri= result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{i} doesn't exist in Spotify. Skipped.")


playlist=sp.user_playlist_create(user=user_id,name=f"{year_here} top 100",public="false")

sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)









#
# spotify=Spotify_Data()
# spotify.get_list()












#
# year="2002-01-02"
# # year=input("Which Year do you want to trvel to in yyyy-MM-DD :")
#
# request=requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}")
# request.raise_for_status()
# data=request.text
# # print(data)
#
#
# soup=BeautifulSoup(data,"html.parser")
# ak=soup.select(selector="li h3#title-of-a-story")
#
# arsenal=[i.getText().strip().strip("\n")  for i in ak ]
# print(arsenal)
#
#
# with open(file="songs.txt",mode="w") as file:
#     for i in arsenal:
#         file.write(f'{i}\n')
#
#
# # # 2002-01-02
#
