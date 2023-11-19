import requests
from bs4 import BeautifulSoup

URL = "https://chapmanganato.com/manga-va998883"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

def get_title():
    raw_title = str(soup.title)

    front_title = raw_title.replace("<title>", '')
    clean_title = front_title.replace("Manga Online Free - Manganato</title>", '')

    print(clean_title)

def get_manga_status():
    tags = soup.find_all('td', class_='table-value')
    
    for tag in tags:
        if "Ongoing" in tag.get_text(strip=True):
            print("Manga Status:", tag.get_text(strip=True))
            break
        elif "Completed" in tag.get_text(strip=True):
            print("Manga Status:", tag.get_text(strip=True))
            break
    else:
        print("Manga status not found.")

genre = ["Action", "Adult", "Adventure", "Comedy", "Cooking", "Doujinshi", "Drama", "Ecchi", "Erotica", "Fantasy", "Gender bender", "Harem", "Historical", "Horror", "Isekai", 
         "Josei", "Manhua", "Martial arts", "Mature", "Mecha", "Medical", "Mystery", "One shot", "Pornographic", "Psychological", "Romance", "School life", "Sci fi", "Seinen", 
         "Shoujo", "Shoujo ai", "Shounen", "Shounen ai", "Slice of life", "Smut", "Sports", "Supernatural", "Tradegy", "Webtoons", "Yaoi", "Yuri"]

def get_genre():
    tags = soup.find_all('td', class_ = 'table-value')
    print("Genre: ")
    for tag in tags:
         if tag.get_text(strip=True) in genre:
            genre_list = tag.get_text(strip=True)
            genres = genre_list.split('-')
            
            for genre_ele in genres:
                print(genre_ele)
            break
get_genre()
