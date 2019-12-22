import urllib
from bs4 import BeautifulSoup
import requests
import urllib.request
from imdb import IMDb
import re

ia = IMDb()


def search_movie(request):
    movies = ia.search_movie(request)
    description = None
    cover_url = None
    try:
        movie = movies[0]
        ia.update(movie, info=['main', 'plot', 'taglines', 'vote details'])

        description = movie.get('title') + '\nScore: ' \
                  + str(movie.get('arithmetic mean')) + '\n' \
                  + re.split(r'::', movie.get('plot')[0], maxsplit=1)[0]
        cover_url = movie['full-size cover url']
    except Exception:
        print("babaH")

    # text = urllib.parse.quote_plus(message.text + 'смотреть онлайн')
    # url = 'https://google.com/search?q=' + text

    # response = requests.get(url)

    # soup = BeautifulSoup(response.text, 'lxml')
    # urls = []
    # for g in soup.find_all("div", class_="kCrYT"):
    #    for t in g.find_all("a", href=True):
    #        if t['href'][:7] != '/search':
    #            urls.append(t['href'][7:])

    # bot.send_message(message.chat.id, '\n'.join(urls[:5]))


    return description, cover_url
