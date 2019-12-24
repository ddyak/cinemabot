import cinemabot_lib.scrapper


def test_scrapper():
    request = "Солярис"
    desc, url = cinemabot_lib.scrapper.search_movie(request)
    assert desc
    assert url
    
