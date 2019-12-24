from imdb import IMDb
from googlesearch import search

import re

ia = IMDb()


def search_movie(request):
    movies = ia.search_movie(request)
    description = None
    cover_url = None
    try:
        movie = movies[0]
        ia.update(movie, info=['main', 'plot', 'taglines', 'vote details'])
        google_request = '{0} {1} смотреть онлайн'.format(movie.get('title'),
                                                          movie.get('year'))

        links = list(search(query=google_request, tld='co.in',
                            lang='ru', num=3, stop=3, pause=1))

        description = '{0} ({1}) {2}/10\n\n{3}\n\n{4}'.format(
            movie.get('title'),
            movie.get('year'),
            movie.get('arithmetic mean'),
            re.split(r'::', movie.get('plot')[0], maxsplit=1)[0],
            '\n'.join(links))

        cover_url = movie['full-size cover url']

    except Exception:
        print(request)

    return description, cover_url

