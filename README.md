# Cinema Bot


**Nickname**: @ddyak\_bot


### Commands

/help - show this info

/start - start command 

[$YOUR_MOVIE] - typical usage


### About implementation

Бот реализован на основе Telebot. При поступлении запроса, мы пытаемся найти фильм на imdb. Для поиска фильма используется библиотека IMDbPy. Если мы его нашли, то забираем оттуда необходимую информацию, и делаем запрос в гугл на поиск ссылок на просмотр фильма, выводим первые три. Бот помещен в докер и задеплоен на AWS.


### Tools, packages, etc...

[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

[IMDbPy](https://imdbpy.github.io/)

[googlesearch](https://github.com/MarioVilas/googlesearch)

[AWS](https://aws.amazon.com/free/faqs/)



### Deploy

```
bash deploy.sh
```
