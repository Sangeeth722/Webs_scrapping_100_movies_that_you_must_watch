import requests
from bs4 import BeautifulSoup

#URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
text_file = response.text

soup = BeautifulSoup(text_file,"html.parser")


find_name = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

movie_list = [item.get_text() for item in find_name]

movie_list.reverse()  # reverse movie_list

with open("movie.txt",mode="w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")



